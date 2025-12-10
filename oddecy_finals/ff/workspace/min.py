#!/usr/bin/env python3
"""
Angr-based solver for Skibidi challenge - Fixed version
"""
import angr
import claripy
import sys

# Import Z3 at module level
try:
    from z3 import *
    Z3_AVAILABLE = True
except ImportError:
    Z3_AVAILABLE = False
    print("[!] Z3 not available, install with: pip3 install z3-solver")

# Import pwntools at module level
try:
    from pwn import *
    PWN_AVAILABLE = True
except ImportError:
    PWN_AVAILABLE = False
    print("[!] pwntools not available, install with: pip3 install pwntools")

def solve():
    binary = "./challenge"
    
    print("[*] Loading binary...")
    # Load binary
    proj = angr.Project(binary, auto_load_libs=False)
    
    # Create symbolic flag
    flag_len = 48
    flag = claripy.BVS('flag', flag_len * 8)
    
    print("[*] Setting up initial state...")
    # Create initial state with symbolic stdin
    state = proj.factory.entry_state(
        stdin=flag
    )
    
    print("[*] Adding constraints...")
    # Add constraints for printable ASCII
    for i in range(flag_len):
        byte = flag.get_byte(i)
        state.add_constraints(claripy.And(byte >= 0x20, byte <= 0x7e))
    
    # Constrain known parts: AKASEC{...}
    state.add_constraints(flag.get_byte(0) == ord('A'))
    state.add_constraints(flag.get_byte(1) == ord('K'))
    state.add_constraints(flag.get_byte(2) == ord('A'))
    state.add_constraints(flag.get_byte(3) == ord('S'))
    state.add_constraints(flag.get_byte(4) == ord('E'))
    state.add_constraints(flag.get_byte(5) == ord('C'))
    state.add_constraints(flag.get_byte(6) == ord('{'))
    state.add_constraints(flag.get_byte(47) == ord('}'))
    
    print("[*] Creating simulation manager...")
    simgr = proj.factory.simulation_manager(state)
    
    print("[*] Exploring... (this may take a while)")
    print("[!] Note: This binary uses dlsym, which may be difficult for angr")
    print("[!] Consider using the alternative approaches below")
    
    # Since the binary uses dlsym heavily, angr might struggle
    # Let's try a different approach - run a limited number of steps
    try:
        # Explore with custom conditions
        def is_successful(state):
            output = state.posix.dumps(1)
            return b"Correct" in output or b"Well done" in output
        
        def is_failed(state):
            output = state.posix.dumps(1)
            return b"Wrong" in output
        
        # Run with timeout
        simgr.explore(
            find=is_successful, 
            avoid=is_failed,
            step_func=lambda sm: sm if len(sm.active) else sm
        )
        
        if simgr.found:
            print("[+] Solution found!")
            solution_state = simgr.found[0]
            solution = solution_state.solver.eval(flag, cast_to=bytes)
            print(f"[+] Flag: {solution.decode('utf-8', errors='ignore')}")
            return solution
        else:
            print("[-] No solution found with angr")
            print("[*] Trying alternative approach...")
            return None
    except Exception as e:
        print(f"[-] Angr failed: {e}")
        print("[*] The binary uses dlsym which is challenging for symbolic execution")
        return None

def manual_solve():
    """
    Manual solving approach - extract the transformations and reverse them
    """
    print("\n" + "="*60)
    print("ALTERNATIVE APPROACH: Manual Analysis")
    print("="*60)
    
    # Expected hash value
    target_hash = 0x4c396c3c
    
    # Expected encrypted bytes (from the binary analysis)
    expected_encrypted = bytes([
        0x18, 0x4c, 0x7c, 0xd0, 0xb8, 0xf4, 0xe5, 0xf4,
        0x4d, 0x8a, 0xa5, 0x46, 0x87, 0x88, 0x18, 0x63,
        0x4a, 0x6d, 0xfa, 0xd9, 0x78, 0x94, 0x05, 0x3e,
        0x7f, 0x98, 0x59, 0x2a, 0xb3, 0x84, 0x75, 0x7e,
        0xd6, 0xf1, 0xa6, 0x2a, 0xd3, 0x94, 0x4c, 0xd7,
        0x36, 0xf1, 0xd1, 0x28, 0xe3, 0x22, 0x0d, 0x7e
    ])
    
    print(f"\nTarget hash: 0x{target_hash:08x}")
    print(f"Expected encrypted length: {len(expected_encrypted)} bytes")
    print(f"Expected encrypted (hex): {expected_encrypted.hex()}")
    
    print("\nTo solve manually:")
    print("1. Use GDB to trace the transformations")
    print("2. Set breakpoint at the comparison loop in validate_flag")
    print("3. Examine what your input becomes after transformation")
    print("4. Reverse engineer the transformation functions")
    print("5. Work backwards from expected_encrypted to original flag")
    
    print("\nGDB Commands:")
    print("  gdb ./challenge")
    print("  break *validate_flag+<offset>  # Set breakpoint at comparison")
    print("  run")
    print("  x/48bx <buffer_address>  # Examine transformed buffer")
    print("  x/48bx <expected_address>  # Examine expected buffer")
    
    print("\nOr try dynamic analysis with frida/LD_PRELOAD to hook dlsym")

def z3_bruteforce():
    """
    Use Z3 to solve the hash equation if we can extract it
    """
    if not Z3_AVAILABLE:
        print("\n[-] Z3 not available")
        return None
        
    print("\n" + "="*60)
    print("Z3 APPROACH: Hash Bruteforce")
    print("="*60)
    
    # The hash function appears to be:
    # for each char: hash = ROL(hash ^ char, 7) ^ 0xdeadbeef
    
    target_hash = 0x4c396c3c
    s = Solver()
    
    # Create symbolic bytes for the flag content (between AKASEC{ and })
    inner_len = 48 - 8  # Total 48, minus "AKASEC{" and "}"
    inner = [BitVec(f'c_{i}', 8) for i in range(inner_len)]
    
    # Constrain to printable ASCII
    for c in inner:
        s.add(And(c >= 0x20, c <= 0x7e))
    
    # Simulate the hash calculation
    # Initial hash value
    h = BitVec('hash', 32)
    s.add(h == 0x12345678)  # From thunk_725adc05
    
    # Process "AKASEC{" 
    prefix = "AKASEC{"
    for ch in prefix:
        h = RotateLeft(h ^ ord(ch), 7) ^ 0xdeadbeef
    
    # Process inner content
    for c in inner:
        h = RotateLeft(h ^ c, 7) ^ 0xdeadbeef
    
    # Process "}"
    h = RotateLeft(h ^ ord('}'), 7) ^ 0xdeadbeef
    
    # Final hash should match target
    s.add(h == target_hash)
    
    print("[*] Solving with Z3... (this may take a while)")
    result = s.check()
    
    if result == sat:
        print("[+] Solution found!")
        model = s.model()
        flag_inner = ''.join(chr(model[c].as_long()) for c in inner)
        flag = f"AKASEC{{{flag_inner}}}"
        print(f"[+] Flag found: {flag}")
        return flag
    elif result == unsat:
        print("[-] No solution exists (constraints are unsatisfiable)")
        return None
    else:
        print("[-] Z3 could not determine satisfiability (timeout/unknown)")
        return None

def dynamic_hook_approach():
    """
    Suggest using dynamic instrumentation
    """
    print("\n" + "="*60)
    print("DYNAMIC INSTRUMENTATION APPROACH")
    print("="*60)
    
    print("""
The best approach for this binary is to use dynamic instrumentation:

1. Use Frida to hook dlsym and log all function resolutions
2. Hook the actual transformation functions
3. Log input/output of each transformation
4. Reverse the transformations

Example Frida script:

```javascript
// Save as hook.js
Interceptor.attach(Module.findExportByName(null, "dlsym"), {
    onEnter: function(args) {
        this.symbol = args[1].readCString();
    },
    onLeave: function(retval) {
        if (this.symbol.startsWith("thunk_")) {
            console.log("dlsym resolved: " + this.symbol + " -> " + retval);
            
            // Hook the resolved function
            Interceptor.attach(retval, {
                onEnter: function(args) {
                    console.log("Calling " + this.symbol);
                }
            });
        }
    }
});
```

Run with: frida -l hook.js ./challenge

Alternatively, use LD_PRELOAD to intercept dlsym.
""")

def simple_test():
    """
    Just try to run the binary and see what happens
    """
    print("\n" + "="*60)
    print("SIMPLE TEST: Running the binary")
    print("="*60)
    
    try:
        from pwn import *
        context.log_level = 'error'
        
        # Try a test flag
        test_flag = "AKASEC{" + "A" * 40 + "}"
        
        p = process('./challenge', level='error')
        p.sendline(test_flag.encode())
        output = p.recvall(timeout=2)
        p.close()
        
        print(f"Test input: {test_flag}")
        print(f"Output: {output.decode('utf-8', errors='ignore')}")
        
    except Exception as e:
        print(f"[-] Could not test: {e}")

if __name__ == "__main__":
    print("="*60)
    print("Skibidi Challenge Solver")
    print("="*60)
    
    # First try simple test
    simple_test()
    
    # Try angr
    print("\n[*] Attempting angr symbolic execution...")
    result = solve()
    
    if not result:
        print("\n[!] Angr approach didn't work (expected due to dlsym)")
        
        # Try Z3
        if Z3_AVAILABLE:
            print("[*] Trying Z3 hash bruteforce...")
            try:
                result = z3_bruteforce()
                if result:
                    print(f"\n[+] SUCCESS! Flag: {result}")
            except Exception as e:
                print(f"[-] Z3 approach failed: {e}")
        
        # Show manual approaches
        if not result:
            manual_solve()
            dynamic_hook_approach()
