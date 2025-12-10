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
known_positions = list(range(7)) + [47]
# Fix: prefix is bytes, convert to list of ints
known_bytes = list(prefix) + [ord('}')]

print(f"Known bytes at positions {known_positions}: {known_bytes}")
print(f"Expected bytes at those positions: {[expected[i] for i in known_positions]}")

# Helper functions
def rot_right(b, shift, bits=8):
    shift %= bits
    return ((b >> shift) | (b << (bits - shift))) & 0xFF

def rot_left(b, shift, bits=8):
    shift %= bits
    return ((b << shift) | (b >> (bits - shift))) & 0xFF

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

# We'll try different orders of operations
def try_order(order, target_bytes, description=""):
    """
    order: list of operation names (in forward order)
    target_bytes: the bytes to reverse (expected or after removing chaining)
    Returns: candidate flag bytes or None if invalid
    """
    candidate = [0] * 48
    for i in range(48):
        b = target_bytes[i]
        # Apply inverse operations in reverse order
        for op_name in reversed(order):
            b = ops[op_name](b, i)
        candidate[i] = b
    flag = bytes(candidate)
    
    # Check known bytes
    all_match = True
    for idx, pos in enumerate(known_positions):
        if flag[pos] != known_bytes[idx]:
            all_match = False
            break
    
    if all_match:
        # Check middle bytes are printable
        middle = flag[7:47]
        if all(32 <= c < 127 for c in middle):
            print(f"\n✓ Found valid flag with {description}")
            print(f"  Order: {order}")
            print(f"  Flag: {flag}")
            return flag
        else:
            # Check what we got anyway
            print(f"\n  Partial match with {description}, order: {order}")
            print(f"  Result: {flag}")
            print(f"  Non-printable in middle: {[c for c in middle if c<32 or c>=127]}")
    return None

# First approach: Try without chaining removal
print("\n" + "="*60)
print("Approach 1: Direct reversal (no chaining)")
print("="*60)

# Based on the thunk_ba9ca5f4 loop, the order might be:
# xor_key, rotate_bits, add_index_times_13, xor_with_66
# But we also have other operations from thunk_3d7f35a6

# Try some likely orders based on the code analysis
likely_orders = [
    # From thunk_ba9ca5f4:
    ['xor_key1', 'rotl3', 'add_idx', 'xor66'],
    ['xor_key2', 'rotl3', 'add_idx', 'xor66'],
    # With additional operations from thunk_3d7f35a6:
    ['xor66', 'rotl3', 'add_idx', 'xor_key1', 'rotl7', 'xor_deadbeef'],
    ['xor66', 'rotl3', 'add_idx', 'xor_key2', 'rotl7', 'xor_deadbeef'],
    ['xor_key1', 'rotl3', 'add_idx', 'xor66', 'rotl7', 'xor_deadbeef'],
    # Reversed order (last operations first):
    ['xor_deadbeef', 'rotl7', 'xor_key1', 'add_idx', 'rotl3', 'xor66'],
]

for order in likely_orders:
    try_order(order, expected, f"direct order {order}")

# Second approach: Try with chaining removal
print("\n" + "="*60)
print("Approach 2: With chaining removal (XOR with previous)")
print("="*60)

# Remove chaining: assume T[i] = X[i] ^ T[i-1] (with T[-1]=0)
X = [0] * 48
X[0] = expected[0]
for i in range(1, 48):
    X[i] = expected[i] ^ expected[i-1]

print("After removing chaining (X[i] = T[i] ^ T[i-1]):")
for i in range(0, 48, 8):
    print(' '.join(f'{b:02x}' for b in X[i:i+8]))

# Try the same orders on X
for order in likely_orders:
    try_order(order, X, f"chaining removed, order {order}")

# Third approach: Try all permutations of a subset of operations
print("\n" + "="*60)
print("Approach 3: Brute-force permutations (limited)")
print("="*60)

# Use a smaller set to keep it manageable
base_ops = ['xor66', 'rotl3', 'add_idx', 'xor_key1', 'rotl7', 'xor_deadbeef']

# We'll try permutations of 4-6 operations
for r in range(4, 7):
    print(f"\nTrying permutations of {r} operations...")
    for perm in itertools.permutations(base_ops, r):
        # Skip if order doesn't seem logical (e.g., xor_deadbeef before others)
        # Just try all
        flag = try_order(list(perm), expected, f"permutation of {r}")
        if flag:
            print(f"Success with permutation: {perm}")
            # Exit if found
            import sys
            sys.exit(0)

# Fourth approach: Try to work backwards from the expected bytes
print("\n" + "="*60)
print("Approach 4: Manual step-by-step reversal")
print("="*60)

# Let's manually try to reverse based on common patterns
# Assume the transformation order is what we see in the loops

# Start from expected
current = expected.copy()
print("Starting from expected bytes:")
for i in range(0, 48, 8):
    print(' '.join(f'{b:02x}' for b in current[i:i+8]))

# Step 1: Remove XOR with 0xDEADBEEF (if it's last)
print("\nStep 1: Try removing XOR with 0xDEADBEEF")
step1 = current.copy()
for i in range(48):
    step1[i] = inv_xor_deadbeef(step1[i], i)

# Step 2: Remove rotate left 7
print("Step 2: Remove rotate left 7")
step2 = step1.copy()
for i in range(48):
    step2[i] = inv_rotl7(step2[i], i)

# Step 3: Remove XOR with key (try both keys)
for key_name in ['xor_key1', 'xor_key2']:
    print(f"\nTrying key: {key_name}")
    step3 = step2.copy()
    for i in range(48):
        if key_name == 'xor_key1':
            step3[i] = inv_xor_key1(step3[i], i)
        else:
            step3[i] = inv_xor_key2(step3[i], i)
    
    # Step 4: Remove add index*13
    step4 = step3.copy()
    for i in range(48):
        step4[i] = inv_add_idx13(step4[i], i)
    
    # Step 5: Remove rotate left 3
    step5 = step4.copy()
    for i in range(48):
        step5[i] = inv_rotl3(step5[i], i)
    
    # Step 6: Remove XOR with 66
    step6 = step5.copy()
    for i in range(48):
        step6[i] = inv_xor66(step6[i], i)
    
    # Check if this gives us a valid flag
    flag = bytes(step6)
    if flag.startswith(prefix) and flag.endswith(suffix):
        print(f"Found flag with key {key_name}: {flag}")
        # Also check middle bytes
        middle = flag[7:47]
        if all(32 <= c < 127 for c in middle):
            print(f"All printable! Flag: {flag}")
            break
    else:
        # Check if at least the known positions match
        known_match = all(flag[pos] == known_bytes[idx] for idx, pos in enumerate(known_positions))
        if known_match:
            print(f"Known positions match with key {key_name}: {flag}")
            print(f"Middle bytes: {flag[7:47]}")

# If still not found, try with chaining included in the manual steps
print("\n" + "="*60)
print("Approach 5: Manual with chaining")
print("="*60)

# Start from expected, remove chaining first
current = expected.copy()
# Remove chaining
unchained = [current[0]] + [current[i] ^ current[i-1] for i in range(1, 48)]

print("After removing chaining:")
for i in range(0, 48, 8):
    print(' '.join(f'{b:02x}' for b in unchained[i:i+8]))

# Now apply the same steps as above
for key_name in ['xor_key1', 'xor_key2']:
    print(f"\nTrying with chaining removed, key: {key_name}")
    step = unchained.copy()
    
    # Apply inverse operations in a likely order
    # Try: xor_deadbeef, rotl7, xor_key, add_idx, rotl3, xor66
    for i in range(48):
        step[i] = inv_xor_deadbeef(step[i], i)
    for i in range(48):
        step[i] = inv_rotl7(step[i], i)
    for i in range(48):
        if key_name == 'xor_key1':
            step[i] = inv_xor_key1(step[i], i)
        else:
            step[i] = inv_xor_key2(step[i], i)
    for i in range(48):
        step[i] = inv_add_idx13(step[i], i)
    for i in range(48):
        step[i] = inv_rotl3(step[i], i)
    for i in range(48):
        step[i] = inv_xor66(step[i], i)
    
    flag = bytes(step)
    if flag.startswith(prefix) and flag.endswith(suffix):
        print(f"Found flag with chaining removed, key {key_name}: {flag}")
        middle = flag[7:47]
        if all(32 <= c < 127 for c in middle):
            print(f"All printable! Flag: {flag}")
            break

print("\n" + "="*60)
print("Summary:")
print("="*60)
print("If no flag was found, the transformation might be more complex.")
print("You may need to:")
print("1. Analyze the binary in a debugger to see the exact transformation order")
print("2. Check if there are additional operations not included here")
print("3. The key might be different than 0x12345678 or 0x4C2D3B7C")
print("\nExpected bytes for reference:")
for i in range(0, 48, 8):
    print(' '.join(f'{b:02x}' for b in expected[i:i+8]))
