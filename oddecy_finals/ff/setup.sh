# setup.sh - Initial setup script
#!/bin/bash

echo "Setting up Reverse Engineering Environment..."

# Create necessary directories
mkdir -p workspace
mkdir -p challenges

# Create a sample GDB init script
cat > workspace/.gdbinit << 'EOF'
# Custom GDB configuration

# Disable confirmation prompts
set confirm off

# Show assembly in Intel syntax
set disassembly-flavor intel

# Auto-load .gdbinit from current directory
set auto-load safe-path /

# Better display
set print pretty on
set print array on
set print array-indexes on

# History
set history save on
set history size 10000
set history filename ~/.gdb_history

# Anti-anti-debug helpers
define hook-stop
    # You can add commands to run on each stop
end

# Custom commands
define patch_nop
    set *(unsigned char*)$arg0 = 0x90
    set *(unsigned char*)($arg0+1) = 0x90
    set *(unsigned char*)($arg0+2) = 0x90
end

document patch_nop
Syntax: patch_nop ADDR
Patches 3 bytes at ADDR with NOPs
end

define skip_call
    set $pc = $pc + 5
end

document skip_call
Skips the current call instruction (5 bytes)
end
EOF

# Create a README
cat > workspace/README.md << 'EOF'
# Reverse Engineering Workspace

## Quick Start

1. Place your binary in `/workspace` or `/challenges`
2. Run analysis: `checksec ./binary`
3. Open in tools:
   - GDB: `gdb ./binary`
   - radare2: `r2 -AA ./binary`
   - Ghidra: `/opt/ghidra/ghidraRun`

## Common Workflows

### Dynamic Analysis with GDB
```bash
gdb ./binary
# In GDB:
> break main
> run
> ni  # next instruction
> si  # step into
> x/10i $rip  # examine 10 instructions
> info registers
```

### Static Analysis with radare2
```bash
r2 -AA ./binary
# In r2:
> aaa  # analyze all
> afl  # list functions
> pdf @ main  # disassemble main
> VV @ main  # visual mode
```

### Symbolic Execution with angr
```python
import angr
proj = angr.Project('./binary', auto_load_libs=False)
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)
simgr.explore(find=SUCCESS_ADDR, avoid=FAIL_ADDR)
```

## Bypassing Anti-Debug

### Method 1: GDB
```bash
gdb ./binary
> source anti_debug.gdb
> run
```

### Method 2: Patching
```bash
python3 /usr/local/bin/patch_binary.py ./binary
./binary.patched
```

### Method 3: LD_PRELOAD
Create a library that hooks ptrace, open, etc.

## Tools Reference

- **checksec**: Check binary security features
- **ROPgadget**: Find ROP gadgets
- **ropper**: Alternative ROP gadget finder
- **one_gadget**: Find one-shot RCE gadgets
- **ltrace**: Trace library calls
- **strace**: Trace system calls
- **pwntools**: Python exploit development

## For the Skibidi Challenge

```bash
# Analyze the binary
checksec ./challenge
r2 -AA ./challenge

# Try to run it
./challenge

# Debug with anti-anti-debug
gdb ./challenge
> source anti_debug.gdb
> break validate_flag
> run
> # Input test flag and examine transformations
```
EOF

# Create example angr solver for skibidi
cat > workspace/skibidi_angr_solver.py << 'EOF'
#!/usr/bin/env python3
"""
Angr-based solver for Skibidi challenge
"""
import angr
import claripy
import sys

def solve():
    binary = "./challenge"
    
    # Load binary
    proj = angr.Project(binary, auto_load_libs=False)
    
    # Create symbolic flag
    flag_len = 48
    flag = claripy.BVS('flag', flag_len * 8)
    
    # Create initial state
    state = proj.factory.entry_state(
        stdin=angr.SimFile('/dev/stdin', content=flag + claripy.BVV(b'\n'))
    )
    
    # Add constraints for printable ASCII
    for i in range(flag_len):
        byte = flag.get_byte(i)
        state.add_constraints(byte >= 0x20, byte <= 0x7e)
    
    # Constrain known parts: AKASEC{...}
    state.add_constraints(flag.get_byte(0) == ord('A'))
    state.add_constraints(flag.get_byte(1) == ord('K'))
    state.add_constraints(flag.get_byte(2) == ord('A'))
    state.add_constraints(flag.get_byte(3) == ord('S'))
    state.add_constraints(flag.get_byte(4) == ord('E'))
    state.add_constraints(flag.get_byte(5) == ord('C'))
    state.add_constraints(flag.get_byte(6) == ord('{'))
    state.add_constraints(flag.get_byte(47) == ord('}'))
    
    # Find addresses (use r2 or ghidra to find these)
    # SUCCESS_ADDR = 0x...  # Where "Correct!" is printed
    # FAIL_ADDR = 0x...     # Where "Wrong!" is printed
    
    print("[*] Creating simulation manager...")
    simgr = proj.factory.simulation_manager(state)
    
    print("[*] Exploring... (this may take a while)")
    # simgr.explore(find=SUCCESS_ADDR, avoid=FAIL_ADDR)
    
    # Alternative: run with custom find condition
    def is_successful(state):
        return b"Correct" in state.posix.dumps(1)
    
    def is_failed(state):
        return b"Wrong" in state.posix.dumps(1)
    
    simgr.explore(find=is_successful, avoid=is_failed)
    
    if simgr.found:
        print("[+] Solution found!")
        solution_state = simgr.found[0]
        solution = solution_state.solver.eval(flag, cast_to=bytes)
        print(f"[+] Flag: {solution.decode('utf-8', errors='ignore')}")
        return solution
    else:
        print("[-] No solution found")
        return None

if __name__ == "__main__":
    solve()
EOF
chmod +x workspace/skibidi_angr_solver.py

echo ""
echo "✓ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Build the image: docker build -t reveng-tools ."
echo "  2. Run the container: docker run -it --rm --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v \$(pwd)/workspace:/workspace reveng-tools"
echo "  3. Or use docker-compose: docker-compose up -d && docker-compose exec reveng /bin/bash"
echo ""
echo "Place your challenge binary in the 'workspace' or 'challenges' directory"