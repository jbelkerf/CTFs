import itertools

# Expected transformed bytes
expected = [
    0xf8, 0xf8, 0xf8, 0xf0, 0xf1, 0xf2, 0xf3, 0xf4,
    0x4d, 0x2c, 0x2b, 0x4d, 0x5c, 0x6b, 0x1d, 0x63,
    0x4a, 0x19, 0x2a, 0x3b, 0x4c, 0x5d, 0x0a, 0x3e,
    0x7f, 0x80, 0x79, 0x7a, 0x7b, 0x7c, 0x7d, 0x7e,
    0xd6, 0x71, 0x82, 0x93, 0xa4, 0xb5, 0xc6, 0xd7,
    0x7e, 0x18, 0x29, 0x3a, 0x4b, 0x5c, 0x0d, 0x7e
]

# Known flag format
prefix = b"AKASEC{"
suffix = b"}"
known_indices = list(range(7)) + [47]
known_bytes = [ord(c) for c in prefix] + [ord('}')]

# Helper functions
def rot_right(b, shift, bits=8):
    shift %= bits
    return ((b >> shift) | (b << (bits - shift))) & ((1 << bits) - 1)

def rot_left(b, shift, bits=8):
    shift %= bits
    return ((b << shift) | (b >> (bits - shift))) & ((1 << bits) - 1)

# Inverse operations
def inv_xor66(b, i):
    return b ^ 66

def inv_rotl3(b, i):
    # forward: (b >> 5) | (b * 8) -> which is rotate left 3
    # inverse: rotate right 3
    return rot_right(b, 3)

def inv_add_idx13(b, i):
    # forward: b + (char)i * 13
    idx = i & 0xFF
    if idx > 127:
        idx -= 256  # signed char
    return (b - idx * 13) & 0xFF

def inv_xor_key1(b, i):
    # key 0x12345678 repeating per byte (little-endian)
    key_bytes = [0x78, 0x56, 0x34, 0x12]
    return b ^ key_bytes[i % 4]

def inv_xor_key2(b, i):
    # key 0x4C2D3B7C (1278831676) repeating
    key_bytes = [0x7C, 0x3B, 0x2D, 0x4C]
    return b ^ key_bytes[i % 4]

def inv_rotl7(b, i):
    # forward: rotate left 7
    # inverse: rotate right 7
    return rot_right(b, 7)

def inv_xor_deadbeef(b, i):
    deadbeef = [0xEF, 0xBE, 0xAD, 0xDE]
    return b ^ deadbeef[i % 4]

# Map operation names to inverse functions
ops = {
    'xor66': inv_xor66,
    'rotl3': inv_rotl3,
    'add_idx': inv_add_idx13,
    'xor_key1': inv_xor_key1,
    'xor_key2': inv_xor_key2,
    'rotl7': inv_rotl7,
    'xor_deadbeef': inv_xor_deadbeef,
}

# We'll try different orders of operations (without chaining)
# Also try with chaining removed first (assuming chaining is the last step)
def try_order(order, target, chain_removed=False):
    """
    order: list of operation names (in forward order)
    target: the bytes to reverse (expected or after removing chaining)
    chain_removed: if True, we already removed chaining, so no need for xor_prev
    Returns: candidate flag bytes or None if invalid
    """
    candidate = [0] * 48
    for i in range(48):
        b = target[i]
        # Apply inverse operations in reverse order
        for op_name in reversed(order):
            b = ops[op_name](b, i)
        candidate[i] = b
    flag = bytes(candidate)
    # Check known bytes
    if all(flag[i] == known_bytes[j] for j, i in enumerate(known_indices)):
        # Check middle bytes are printable
        if all(32 <= c < 127 for c in flag[7:47]):
            return flag
    return None

# First, try without chaining removal (i.e., assume no chaining in transformation)
print("Trying without chaining removal...")
# We'll try all permutations of a subset of operations. Let's use 6 operations at a time.
op_names = ['xor66', 'rotl3', 'add_idx', 'xor_key1', 'rotl7', 'xor_deadbeef']
found = False
for perm in itertools.permutations(op_names):
    flag = try_order(perm, expected, chain_removed=False)
    if flag:
        print(f"Found flag with order {perm}: {flag}")
        found = True
        break

if not found:
    # Try with xor_key2 instead of xor_key1
    op_names2 = ['xor66', 'rotl3', 'add_idx', 'xor_key2', 'rotl7', 'xor_deadbeef']
    for perm in itertools.permutations(op_names2):
        flag = try_order(perm, expected, chain_removed=False)
        if flag:
            print(f"Found flag with order {perm}: {flag}")
            found = True
            break

# If still not found, try with chaining removal
# Assume chaining is the last step: T[i] = X[i] ^ T[i-1] (with T[-1]=0)
# So we compute X[i] = T[i] ^ T[i-1]
if not found:
    print("\nTrying with chaining removal...")
    X = [0] * 48
    X[0] = expected[0]
    for i in range(1, 48):
        X[i] = expected[i] ^ expected[i-1]
    # Now try orders on X
    for perm in itertools.permutations(op_names):
        flag = try_order(perm, X, chain_removed=True)
        if flag:
            print(f"Found flag with order {perm} (chaining removed): {flag}")
            found = True
            break
    if not found:
        for perm in itertools.permutations(op_names2):
            flag = try_order(perm, X, chain_removed=True)
            if flag:
                print(f"Found flag with order {perm} (chaining removed): {flag}")
                found = True
                break

# If still not found, maybe the order includes all 7 operations? Let's try with 7 operations.
if not found:
    print("\nTrying all 7 operations...")
    all_ops = ['xor66', 'rotl3', 'add_idx', 'xor_key1', 'rotl7', 'xor_deadbeef']  # 6, but we can add xor_key2? Actually we already tried two sets.
    # We'll try permutations of 6 ops from the set of 7 (including both keys) but that's many.
    # Let's try a different approach: use the known bytes to deduce the transformation per byte.
    # We'll brute-force the order for each byte? Too heavy.
    pass

# If still no luck, maybe the transformation includes the "complex math" operation which we haven't modeled.
# From the decompiled code, thunk_6adc8c29 does: *(a0) = *(a0) + (*(a2) + 1) * *(a1). That's complicated.

# Given the time, let's try a manual approach: assume the transformation is as in thunk_ba9ca5f4:
# forward order: xor_with_key, copy_byte, rotate_bits, add_index_times_13, xor_with_66, store_result.
# But copy_byte and store_result are just moves, so the actual operations are: xor_key, rotate_bits, add_idx, xor_66.
# Then maybe after that, there is chaining and xor_deadbeef? Not sure.

# Let's try a specific order that seems plausible from the code:
# From thunk_ba9ca5f4: xor_key, rotate_bits, add_idx, xor_66.
# From thunk_3d7f35a6: load, set0, complex_math, rol7, xor, xor_deadbeef.
# Combining: maybe the full transformation is: xor66, rotl3, add_idx, xor_key, rol7, xor_deadbeef, then chain? Or chain in between.

# Let's try a few hardcoded orders:
print("\nTrying hardcoded orders...")
orders_to_try = [
    ['xor66', 'rotl3', 'add_idx', 'xor_key1', 'rotl7', 'xor_deadbeef'],
    ['xor66', 'rotl3', 'add_idx', 'xor_key1', 'rotl7', 'xor_deadbeef', 'xor_prev'],  # with chaining as last
    ['xor_key1', 'rotl3', 'add_idx', 'xor66', 'rotl7', 'xor_deadbeef'],
    ['xor66', 'rotl3', 'add_idx', 'xor_key1', 'xor_deadbeef', 'rotl7'],
    ['xor_deadbeef', 'rotl7', 'xor_key1', 'add_idx', 'rotl3', 'xor66'],  # reverse of first
]

# For orders with xor_prev, we need to handle chaining specially.
def try_order_with_chain(order, target):
    # Assume xor_prev is in the order. We'll remove its effect first if it's last?
    # Actually, if xor_prev is the last operation forward, then target already includes chaining.
    # So we need to remove chaining before applying other inverses if xor_prev is last.
    # But we already tried removing chaining uniformly. Let's assume xor_prev is at a specific position.
    # We'll assume xor_prev is the last operation in forward order.
    if order[-1] == 'xor_prev':
        # Remove chaining
        X = [0] * 48
        X[0] = target[0]
        for i in range(1, 48):
            X[i] = target[i] ^ target[i-1]
        # Now reverse other ops
        other_ops = order[:-1]
        candidate = [0] * 48
        for i in range(48):
            b = X[i]
            for op_name in reversed(other_ops):
                b = ops[op_name](b, i)
            candidate[i] = b
        flag = bytes(candidate)
        if all(flag[i] == known_bytes[j] for j, i in enumerate(known_indices)):
            if all(32 <= c < 127 for c in flag[7:47]):
                return flag
    return None

for order in orders_to_try:
    if 'xor_prev' in order:
        flag = try_order_with_chain(order, expected)
    else:
        flag = try_order(order, expected, chain_removed=False)
    if flag:
        print(f"Found with order {order}: {flag}")
        found = True
        break

if not found:
    print("Could not find flag with automated permutations.")
    print("You may need to analyze the binary more to get the exact transformation order.")
    print("However, based on common patterns and the challenge, the flag might be:")
    print("AKASEC{limon_obfuscation_is_fun_but_reverse_is_harder}")
    print("But that's just a guess. Let's try to compute the flag by brute-forcing the middle bytes?")
    # Alternatively, we can try to use the fact that the flag must be printable and the transformation is likely invertible.
    # We can try to brute-force the transformation by trying all possible orders and parameters for the known bytes and see if the same order works for all bytes.
    # But that's what we already did to some extent.

# Let's output the expected bytes for reference:
print("\nExpected transformed bytes (hex):")
for i in range(0, 48, 8):
    print(' '.join(f'{b:02x}' for b in expected[i:i+8]))
