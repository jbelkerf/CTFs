#!/usr/bin/env python3

# Encrypted data from sub_401360
v1 = 3327582826336971941963127324716
v2 = 4278320777412034452680242888724
v3 = 1584563251355197908386551169052
v4 = 4753689751224795137155547529276
v5 = 1584563251133836979343122759696
v6 = 292057776154

# Combine all values into bytes (little-endian)
def int_to_bytes(n, size):
    """Convert integer to bytes in little-endian format"""
    return n.to_bytes(size, byteorder='little')

# Extract bytes from each integer
bytes_data = b''
bytes_data += int_to_bytes(v1, 16)  # 128-bit = 16 bytes
bytes_data += int_to_bytes(v2, 16)
bytes_data += int_to_bytes(v3, 16)
bytes_data += int_to_bytes(v4, 16)
bytes_data += int_to_bytes(v5, 16)
bytes_data += int_to_bytes(v6, 16)

print("Encrypted bytes:", bytes_data.hex())
print("Length:", len(bytes_data))

# Decrypt by subtracting 80 from each byte
decrypted = bytes([(b - 80) % 256 for b in bytes_data[:20]])  # v7 = 20 (length)

print("\nDecrypted password:", decrypted.decode('ascii', errors='ignore'))
print("Hex:", decrypted.hex())

# Alternative: try different endianness if above doesn't work
print("\n--- Alternative (big-endian) ---")
bytes_data_be = b''
bytes_data_be += int_to_bytes(v1, 16)
bytes_data_be += int_to_bytes(v2, 16) 
bytes_data_be += int_to_bytes(v3, 16)
bytes_data_be += int_to_bytes(v4, 16)
bytes_data_be += int_to_bytes(v5, 16)
bytes_data_be += int_to_bytes(v6, 16)

decrypted_alt = bytes([(b - 80) % 256 for b in bytes_data_be[:20]])
print("Alternative password:", decrypted_alt.decode('ascii', errors='ignore'))
