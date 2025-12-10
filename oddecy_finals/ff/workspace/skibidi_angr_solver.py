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
