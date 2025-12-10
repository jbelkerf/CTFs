import struct

def ror(val, n):
    """Rotate Right (8-bit)"""
    return ((val >> n) | (val << (8 - n))) & 0xFF

# 1. The Encrypted Bytes
# ---------------------------------------------------
# These are extracted from the stack setup thunks in validate_flag
target_hex = [
    0xf4e5f4b8d07c4c18, 0x6318888746a58a4d, 
    0x3e059478d9fa6d4a, 0x7e7584b32a59987f, 
    0xd74c94d32aa6f1d6, 0x7e0d22e328d1f136
]

# Convert Little Endian hex chunks to a byte array
encrypted = bytearray()
for val in target_hex:
    encrypted.extend(struct.pack('<Q', val))

print(f"[*] Encrypted Length: {len(encrypted)}")
print(f"[*] Encrypted Hex: {encrypted.hex()}")

# 2. Decryption Logic
# ---------------------------------------------------
flag = bytearray(len(encrypted))

for i in range(len(encrypted)):
    # Start with the encrypted byte
    char = encrypted[i]
    
    # Step 5: Reverse "XOR with Prev"
    # Note: In encryption, this uses the PREVIOUS result (encrypted[i-1]).
    # So we just XOR with the known encrypted byte at i-1.
    if i > 0:
        char ^= encrypted[i-1]
    
    # Step 4: Reverse "XOR with i"
    char ^= i
    
    # Step 3: Reverse "ADD (i * 13)"
    # We subtract, handling modulo 256
    sub_val = (i * 13) % 256
    char = (char - sub_val) & 0xFF
    
    # Step 2: Reverse "Rotate Left 3" -> Rotate Right 3
    char = ror(char, 3)
    
    # Step 1: Reverse "XOR 0x42"
    char ^= 0x42
    
    flag[i] = char

# 3. Output
# ---------------------------------------------------
print(f"\n[+] Flag: {flag.decode('latin-1')}")
