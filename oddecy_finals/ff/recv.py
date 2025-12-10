import struct

# 1. Simulate the C logic for rand() and skibidi_thunker
# -----------------------------------------------------
class PRNG:
    def __init__(self, seed):
        self.state = seed

    def rand(self):
        # Glibc Linear Congruential Generator
        self.state = (self.state * 1103515245 + 12345) & 0x7FFFFFFF
        return self.state

# Initialize RNG with the seed found in main/setup
rng = PRNG(0x7141beef)
cache = {} # To simulate the skibidi cache

def get_thunk_name(param_id):
    if param_id in cache:
        return cache[param_id]
    
    r = rng.rand()
    # Logic from decompilation: name = "thunk_%x" % (rand_val ^ param_id)
    val = r ^ param_id
    name = f"thunk_{val:x}"
    cache[param_id] = name
    return name

# 2. Reconstruct the Execution Flow to sync the RNG
# -----------------------------------------------------
# We must process the IDs in the EXACT order they appear in the binary
# so our RNG stays in sync with the real program.

# Sequence of IDs based on decompilation reading:
execution_sequence = [
    # main start
    0xf907c6c5, 0x3bcd69f8, 
    # if fgets fails (skipped)
    # else block
    0xb059b28e, 
    # validate_flag start
    0x111743b0, # strlen/copy
    0x5a7bb9be, # checksum wrapper
    # Inside checksum wrapper (thunk_4ff37435)
    0x4ff37435,
        # Inside checksum LOOP init (thunk_3d7f35a6)
        0x41d85547, 0xc92041f,
        # Inside checksum LOOP body (runs 48 times, but cached after first)
        0xaad2441d, 0xa3498423, 0x22bfd2d4, 0x7e78d71a, 0x6b507c1f,
    # Back to validate_flag (Success path)
    0x431b1ca8, # stack setup 1
    0x61f81883, # stack setup 2
    0x25d4225b, # stack setup 3
    0xe97d51f3, # stack setup 4
    0x81f7df3b, # stack setup 5
    0xfba563c0, # stack setup 6
    0xa9067e26, # Call encryption wrapper
    0x554a00d1, # thunk_3d1fe6cf (Wrapper)
    0x315c3182, # thunk_ba9ca5f4 (The Encryption Loop!)
        # Inside Encryption Loop (thunk_ba9ca5f4)
        0x373e6916, # init i=1
        # LOOP BODY IDs:
        0xf887fb13, 
        0x17e7045b, 
        0x6459a6c9, 
        0xd8969d87, 
        0xf33f8677, 
        0x3d4987fe  # likely loop increment/check
]

# Run the simulation to map IDs to Names
thunk_map = {}
for pid in execution_sequence:
    thunk_map[pid] = get_thunk_name(pid)

print("[*] Mapped Encryption Thunks:")
encryption_ops = [
    0xf887fb13, 0x17e7045b, 0x6459a6c9, 0xd8969d87, 0xf33f8677
]

for pid in encryption_ops:
    print(f"  ID {pid:x} -> {thunk_map[pid]}")

# 3. Decrypt the Flag
# -----------------------------------------------------
# Based on the output above, we map the C code logic to these names:
# 0xf887fb13 -> thunk_5667b8fe: buf[i] ^= buf[i-1]
# 0x17e7045b -> thunk_f49b6b4b: buf[i] += i * 13
# 0x6459a6c9 -> thunk_2f731ec9: buf[i] = ROL(buf[i], 3)
# 0xd8969d87 -> thunk_7d676f54: buf[i] ^= 0x42
# 0xf33f8677 -> thunk_8146f783: buf[i] ^= i

# Helper for Bit Rotation (8-bit)
def rol(x, n):
    return ((x << n) | (x >> (8 - n))) & 0xFF

def ror(x, n):
    return ((x >> n) | (x << (8 - n))) & 0xFF

# The Hardcoded Encrypted Bytes (Little Endian from stack sets)
# Extracted from:
# thunk_4dd7fda5 (0x00): f4e5f4b8d07c4c18
# thunk_b618cce9 (0x08): 6318888746a58a4d
# thunk_ed211175 (0x10): 3e059478d9fa6d4a
# thunk_a8cd2ab6 (0x18): 7e7584b32a59987f
# thunk_8fcfc1a9 (0x20): d74c94d32aa6f1d6
# thunk_7c444269 (0x28): 7e0d22e328d1f136

target_hex = [
    0xf4e5f4b8d07c4c18, 0x6318888746a58a4d, 
    0x3e059478d9fa6d4a, 0x7e7584b32a59987f, 
    0xd74c94d32aa6f1d6, 0x7e0d22e328d1f136
]

target_bytes = bytearray()
for val in target_hex:
    target_bytes.extend(struct.pack('<Q', val))

print(f"\n[*] Target Bytes: {target_bytes.hex()}")

# We decrypt assuming the loop runs from i=1 to 47
# buf[0] is 'A' (0x41) and is NOT modified by the loop structure.
# But... Target[0] is 0x18.
# This implies Target[0] IS encrypted.
# Looking closer at decompilation: 'AKASEC{' check happens first.
# BUT the loop structure suggests propagation.
# Let's brute force index 0 if needed, but for now we assume standard CBC.
# Reverse Order of operations:
# Forward: XOR i -> XOR 0x42 -> ROL 3 -> ADD(i*13) -> XOR prev
# Inverse: XOR prev -> SUB(i*13) -> ROR 3 -> XOR 0x42 -> XOR i

flag = bytearray(48)
flag[0] = target_bytes[0] # Assume index 0 is static? Or check math.
# Actually, let's just reverse index 1..47 first.
# For index 0, let's assume it matches 'A' and see if it propagates correctly.

# Wait, if loop is 1..47, how did Target[0] become 0x18? 
# Maybe the hardcoded values are obfuscated too? 
# Let's trust the logic: buf[i] depends on buf[i-1].
# We treat target_bytes as the Final State.

# Recovery Loop
recovered = bytearray(48)
recovered[0] = 0x41 # 'A'

for i in range(1, 48):
    y = target_bytes[i]
    
    # 1. Reverse XOR i
    y ^= i
    
    # 2. Reverse XOR 0x42
    y ^= 0x42
    
    # 3. Reverse ROL 3 (Use ROR 3)
    y = ror(y, 3)
    
    # 4. Reverse ADD (i * 13)
    val_to_sub = (i * 13) % 256
    y = (y - val_to_sub) & 0xFF
    
    # 5. Reverse XOR with Previous (CBC)
    # Important: In encryption, it used the *modified* previous byte.
    # So we XOR with target_bytes[i-1]
    y ^= target_bytes[i-1]
    
    recovered[i] = y

print(f"\n[+] Flag: {recovered.decode('latin-1')}")
