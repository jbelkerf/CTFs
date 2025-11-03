from pwn import *


r = remote("165.22.86.44", 33083)

print(r.recvline())
