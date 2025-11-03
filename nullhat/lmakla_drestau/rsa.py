#!/usr/bin/env python3
from pwn import *
import math

def factorize(n):
    """Factorize n into two primes p and q"""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = i
            q = n // i
            # Verify both are prime
            if all(p % j != 0 for j in range(2, int(math.sqrt(p)) + 1)) and \
               all(q % j != 0 for j in range(2, int(math.sqrt(q)) + 1)):
                return p, q
    return None, None

def solve_challenge():
    # Connect to the server
    conn = remote('165.22.86.44', 33083)
    
    # Receive the banner and parameters
    data = conn.recvuntil(b'Enter p:').decode()
    print(data)
    
    # Parse n and e from the received data
    n_match = re.search(r'n = (\d+)', data)
    e_match = re.search(r'e = (\d+)', data)
    
    if not n_match or not e_match:
        print("Failed to parse parameters")
        return
    
    n = int(n_match.group(1))
    e = int(e_match.group(1))
    
    print(f"[*] Extracted parameters: n={n}, e={e}")
    
    # Factorize n
    p, q = factorize(n)
    
    if p is None:
        print(f"[-] Failed to factorize n={n}")
        return
    
    print(f"[+] Factorization successful: p={p}, q={q}")
    print(f"[*] Verification: {p} * {q} = {p*q} (should be {n})")
    
    # Send the factors
    conn.sendline(str(p).encode())
    conn.recvuntil(b'Enter q:')
    conn.sendline(str(q).encode())
    
    # Continue the interaction
    try:
        while True:
            response = conn.recvline(timeout=2).decode()
            print(response, end='')
    except:
        print("\n[*] Connection finished")
    
    conn.close()

if __name__ == "__main__":
    solve_challenge()