#!/usr/bin/env python3
from pwn import *
import math
import re

def factorize(n):
    """Factorize n into two primes p and q"""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = i
            q = n // i
            if all(p % j != 0 for j in range(2, int(math.sqrt(p)) + 1)) and \
               all(q % j != 0 for j in range(2, int(math.sqrt(q)) + 1)):
                return p, q
    return None, None

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """Find modular inverse using extended Euclidean algorithm"""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        return None
    return x % phi

def solve_complete():
    conn = remote('165.22.86.44', 33083)
    
    # Phase 1: Get initial data and factorize
    data = conn.recvuntil(b'Enter p:').decode()
    print(data)
    
    # Parse n and e
    n_match = re.search(r'n = (\d+)', data)
    e_match = re.search(r'e = (\d+)', data)
    n = int(n_match.group(1))
    e = int(e_match.group(1))
    
    print(f"[*] n={n}, e={e}")
    
    # Factorize
    p, q = factorize(n)
    print(f"[+] p={p}, q={q}")
    
    # Send factors
    conn.sendline(str(p).encode())
    conn.recvuntil(b'Enter q:')
    conn.sendline(str(q).encode())
    
    # Phase 2: Euler's Totient
    conn.recvuntil(b'Calculate phi(n) = (p-1)(q-1)')
    phi = (p - 1) * (q - 1)
    print(f"[+] phi(n) = {phi}")
    conn.sendline(str(phi).encode())
    
    # Handle CAPTCHA - wait for user input
    captcha_data = conn.recvuntil(b'Enter it:').decode()
    print(captcha_data)
    
    # Wait for user to manually enter the CAPTCHA
    captcha_number = input("Enter the number you see in the ASCII art: ")
    conn.sendline(captcha_number.encode())
    
    # Phase 3: Private Key Generation
    conn.recvuntil(b'Find d where: d * e ')
    d = mod_inverse(e, phi)
    print(f"[+] Calculating private key d = {e}^(-1) mod {phi} = {d}")
    conn.sendline(str(d).encode())
    
    # Wait for Final Phase: Flag Decryption
    final_phase = conn.recvuntil(b'Enter the decrypted flag :').decode()
    print(final_phase)
    
    # Parse encrypted flag from initial data
    flag_match = re.search(r'Encrypted flag:\s*\[([\d,\s]+)\]', data)
    if flag_match:
        encrypted_flag_str = flag_match.group(1)
        encrypted_flag = [int(x.strip()) for x in encrypted_flag_str.split(',')]
        print(f"[*] Encrypted flag: {encrypted_flag}")
        
        # Decrypt the flag
        decrypted_bytes = []
        for ct in encrypted_flag:
            pt = pow(ct, d, n)
            decrypted_bytes.append(pt)
        
        print(f"[*] Decrypted bytes: {decrypted_bytes}")
        
        # Convert to text
        try:
            flag_text = ''.join(chr(byte) for byte in decrypted_bytes)
            print(f"[+] Decrypted flag: {flag_text}")
            print(f"[+] Sending flag: {flag_text}")
            conn.sendline(flag_text.encode())
        except:
            print("[-] Could not convert to ASCII")
            flag_str = ' '.join(str(byte) for byte in decrypted_bytes)
            print(f"[+] Sending decrypted numbers: {flag_str}")
            conn.sendline(flag_str.encode())
    
    # Get final output
    try:
        final_output = conn.recvall(timeout=5).decode()
        print(final_output)
    except:
        pass
    
    conn.close()

if __name__ == "__main__":
    solve_complete()