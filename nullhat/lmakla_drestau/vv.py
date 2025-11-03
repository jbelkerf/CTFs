#!/usr/bin/env python3

# Encrypted data from sub_401360
v1 = 3327582826336971941963127324716
v2 = 4278320777412034452680242888724
v3 = 1584563251355197908386551169052
v4 = 4753689751224795137155547529276
v5 = 1584563251133836979343122759696
v6 = 292057776154

length = 20

print("="*60)
print("CTF Challenge Password Decryptor")
print("="*60)

def try_decrypt(data_bytes, name):
    """Try to decrypt bytes by subtracting 80"""
    try:
        decrypted = bytes([(b - 80) & 0xFF for b in data_bytes[:length]])
        result = decrypted.decode('ascii', errors='replace')
        
        print(f"\n{name}:")
        print(f"  Raw bytes: {data_bytes[:length].hex()}")
        print(f"  Decrypted: '{result}'")
        print(f"  Hex: {decrypted.hex()}")
        
        # Check if it looks like readable text
        printable = sum(32 <= b < 127 for b in decrypted)
        print(f"  Printable: {printable}/{length} chars")
        
        return result, printable
    except Exception as e:
        print(f"{name}: Error - {e}")
        return None, 0

# Method 1: Little-endian (most common for x86-64)
print("\n" + "="*60)
print("METHOD 1: Little-endian concatenation")
print("="*60)

data_le = b''
for val in [v1, v2, v3, v4, v5, v6]:
    data_le += val.to_bytes(16, byteorder='little')

result1, score1 = try_decrypt(data_le, "Little-endian")

# Method 2: Big-endian
print("\n" + "="*60)
print("METHOD 2: Big-endian concatenation")
print("="*60)

data_be = b''
for val in [v1, v2, v3, v4, v5, v6]:
    data_be += val.to_bytes(16, byteorder='big')

result2, score2 = try_decrypt(data_be, "Big-endian")

# Method 3: Packed as 32-bit integers (common in decompilers)
print("\n" + "="*60)
print("METHOD 3: 32-bit integer array")
print("="*60)

# Extract 4-byte chunks from the 128-bit values
def extract_dwords(val):
    """Extract four 32-bit values from a 128-bit integer"""
    dwords = []
    for i in range(4):
        dwords.append((val >> (i * 32)) & 0xFFFFFFFF)
    return dwords

data_dword = b''
for val in [v1, v2, v3, v4, v5, v6]:
    for dword in extract_dwords(val):
        data_dword += dword.to_bytes(4, byteorder='little')

result3, score3 = try_decrypt(data_dword, "32-bit DWORDs")

# Method 4: Try reversing byte order within each 128-bit block
print("\n" + "="*60)
print("METHOD 4: Reversed within 128-bit blocks")
print("="*60)

data_rev = b''
for val in [v1, v2, v3, v4, v5, v6]:
    block = val.to_bytes(16, byteorder='little')
    data_rev += block[::-1]  # Reverse each 16-byte block

result4, score4 = try_decrypt(data_rev, "Block-reversed")

# Method 5: Just the first 20 bytes of v1-v6 concatenated (variable-length encoding)
print("\n" + "="*60)
print("METHOD 5: Direct byte extraction (minimal)")
print("="*60)

all_vals = [v1, v2, v3, v4, v5, v6]
data_direct = b''.join(val.to_bytes((val.bit_length() + 7) // 8, 'little') for val in all_vals)

result5, score5 = try_decrypt(data_direct, "Direct minimal")

# Find best result
print("\n" + "="*60)
print("BEST CANDIDATE")
print("="*60)

results = [
    (result1, score1, "Little-endian"),
    (result2, score2, "Big-endian"),
    (result3, score3, "32-bit DWORDs"),
    (result4, score4, "Block-reversed"),
    (result5, score5, "Direct minimal")
]

best = max(results, key=lambda x: x[1])
print(f"\nMost likely password ({best[2]}): '{best[0]}'")
print(f"Printable score: {best[1]}/{length}")

print("\n" + "="*60)
print("Try running:")
print("  echo '{}' | ./challenge".format(best[0]))
print("="*60)
