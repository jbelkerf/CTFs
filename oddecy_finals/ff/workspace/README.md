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
