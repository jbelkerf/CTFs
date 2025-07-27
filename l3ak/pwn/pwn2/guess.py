from pwn import *
import ctypes
import time

libc = ctypes.CDLL("libc.so.6")

seed = libc.srand(int(time.time()))
v4 = libc.rand(seed)

nhonks = v4 % 91 + 10

p = process("./chall")
# p.sendlineafter()
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())

# p.sendline(b"jbelkerf")

time.sleep(0.2)# print(p.recvline())
p.sendline( b"jbelkerf")

print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())