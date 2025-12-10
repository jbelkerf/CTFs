import struct
import itertools

# ---------------------------------------------------
# 1. The Ciphertext (Extracted from the thunk_ calls)
# ---------------------------------------------------
target_hex = [
    0xf4e5f4b8d07c4c18, 0x6318888746a58a4d, 
    0x3e059478d9fa6d4a, 0x7e7584b32a59987f, 
    0xd74c94d32aa6f1d6, 0x7e0d22e328d1f136
]
ciphertext = bytearray()
for val in target_hex:
    ciphertext.extend(struct.pack('<Q', val))

# ---------------------------------------------------
# 2. The Math Operations (From decompiled source)
# ---------------------------------------------------
# We implement the operations found in the provided C code.

def op_xor_prev(buf, i): # thunk_5667b8fe
    if i > 0: buf[i] ^= buf[i-1]

def op_add_idx_13(buf, i): # thunk_f49b6b4b
    buf[i] = (buf[i] + (i * 13)) & 0xFF

def op_rol_3(buf, i): # thunk_2f731ec9 (>>5 | <<3 is ROL 3)
    val = buf[i]
    buf[i] = ((val << 3) | (val >> 5)) & 0xFF

def op_xor_42(buf, i): # thunk_7d676f54
    buf[i] ^= 0x42

def op_xor_idx(buf, i): # thunk_8146f783
    buf[i] ^= i

# List of available operations
ALL_OPS = [op_xor_prev, op_add_idx_13, op_rol_3, op_xor_42, op_xor_idx]

# ---------------------------------------------------
# 3. Brute Force the Order
# ---------------------------------------------------
known_prefix = b"AKASEC{"

print("[*] Brute-forcing operation order...")

# We need to find two permutations: one for Layer 1, one for Layer 2.
# We test them by encrypting "AKASEC{" and checking if it matches ciphertext[0:7]

correct_layer1 = None
correct_layer2 = None

# optimization: The loops in the binary run 1..N-1
# Index 0 is often skipped or processed differently. 
# Based on the binary, the loops iterate `local_c` from start to end.
# We'll assume the loop processes indices 0 to 6 for the prefix check.

for p1 in itertools.permutations(ALL_OPS):
    for p2 in itertools.permutations(ALL_OPS):
        
        # Test candidate
        test_buf = bytearray(known_prefix)
        
        # Apply Layer 1
        for i in range(len(test_buf)):
            for op in p1:
                op(test_buf, i)
        
        # Apply Layer 2
        for i in range(len(test_buf)):
            for op in p2:
                op(test_buf, i)
                
        # Check match
        if test_buf == ciphertext[:7]:
            print(f"[+] Found correct permutations!")
            correct_layer1 = p1
            correct_layer2 = p2
            break
    if correct_layer1: break

if not correct_layer1:
    print("[-] Failed to find permutation. Checking assumptions...")
    # Fallback: Maybe index 0 is skipped? The loop usually starts at 0 or 1.
    # If the above failed, manual reversing of index 0 might be needed, 
    # but let's try to decrypt with what we have if partial match.
    exit()

# ---------------------------------------------------
# 4. Decrypt the Full Flag
# ---------------------------------------------------
# To decrypt, we must reverse the layers in REVERSE order (Layer 2 then Layer 1)
# And within each layer, reverse the operations in REVERSE order.
# And reverse the math (Add -> Sub, Rol -> Ror).

def rev_op_xor_prev(buf, i):
    # For decryption of index i, we need the *encrypted* state of i-1.
    # Since we decrypt backwards or just invert the logic?
    # Actually, XOR is self-inverse. BUT, the encryption used the modified prev.
    # So during decryption (which goes 0..N), we use the current byte at i-1.
    if i > 0: buf[i] ^= buf[i-1]

def rev_op_add_idx_13(buf, i):
    val = (buf[i] - (i * 13))
    buf[i] = val % 256

def rev_op_rol_3(buf, i): # Reverse of ROL 3 is ROR 3
    val = buf[i]
    buf[i] = ((val >> 3) | (val << 5)) & 0xFF

def rev_op_xor_42(buf, i):
    buf[i] ^= 0x42

def rev_op_xor_idx(buf, i):
    buf[i] ^= i

# Map forward ops to reverse ops
rev_map = {
    op_xor_prev: rev_op_xor_prev,
    op_add_idx_13: rev_op_add_idx_13,
    op_rol_3: rev_op_rol_3,
    op_xor_42: rev_op_xor_42,
    op_xor_idx: rev_op_xor_idx
}

# Construct reverse pipelines
pipeline1 = [rev_map[op] for op in reversed(correct_layer1)]
pipeline2 = [rev_map[op] for op in reversed(correct_layer2)]

# Decrypt Buffer (Copy ciphertext)
flag = bytearray(ciphertext)

# Invert Layer 2
for i in range(len(flag)):
    for op in pipeline2:
        op(flag, i)

# Invert Layer 1
for i in range(len(flag)):
    for op in pipeline1:
        op(flag, i)

print(f"\n[+] Flag: {flag.decode('latin-1')}")
