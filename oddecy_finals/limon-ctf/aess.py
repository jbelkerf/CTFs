from pwn import *
from binascii import unhexlify, hexlify
import random
import time
import sys

# --- Target Configuration ---
HOST = '10.25.1.156'
PORT = 8888
# ----------------------------

# This class must MATCH the challenge code exactly to replicate the logic locally
class feedfront:
    def __init__(self, size):
        self.size = size
        # We don't init state here because we will inject the synced state later
        self.state = 0 
        
    def set_state(self, seed_val):
        # Re-seed the global random module to match the server
        random.seed(seed_val)
        self.state = random.getrandbits(self.size)

    def next_state(self):
        # Exact logic from challenge
        tap = random.randint(1, self.size - 1)
        term1 = (self.state >> 13)
        term2 = (self.state >> 37)
        term3 = (self.state >> tap)
        feedback = (term1 ^ term2 ^ term3) & 1
        self.state = (self.state >> 1) | (feedback << (self.size - 1))

    def get_byte(self):
        b_data = 0
        while b_data == 0:
            for _ in range(8):
                lsb = self.state & 1
                b_data = (b_data << 1) | lsb
                self.next_state()
        return b_data

    def encrypt(self, data):
        key = []
        for _ in range(len(data)):
            key.append(self.get_byte())
        
        return bytes([x ^ y for x, y in zip(data, key)])

def solve():
    print(f"[*] Connecting to {HOST}:{PORT}...")
    r = remote(HOST, PORT)

    # 1. Get the approximate timestamp of connection
    # The server likely seeded 'random' with time.time() around this moment.
    now = int(time.time())
    
    # Receive the banner and the key leak
    # (We read until the menu appears to ensure the buffer is clean)
    r.recvuntil(b">> ")
    
    # 2. Extract the Keystream
    # We send 32 bytes of Null (\x00). 
    # Since Cipher = Plain XOR Key, if Plain is 0, Cipher = Key.
    payload_len = 32
    zeros = b'\x00' * payload_len
    
    r.sendline(b"1")             # Select Option 1
    r.recvuntil(b"data: ")
    r.sendline(hexlify(zeros))   # Send hex-encoded zeros
    
    r.recvuntil(b"c1 = ")
    c1_output = r.recvline().strip().decode()
    server_keystream = unhexlify(c1_output)
    
    print(f"[+] Captured server keystream sample: {c1_output[:20]}...")

    # 3. Brute-force the Seed
    # We try seeds from (now - 120s) to (now + 120s) to account for clock differences.
    print("[*] Brute-forcing random seed...")
    
    found_seed = None
    cipher_clone = feedfront(64)
    
    for offset in range(-120, 120):
        seed_candidate = now + offset
        
        # Test this seed
        cipher_clone.set_state(seed_candidate)
        
        # Generate a keystream with this seed
        # We must encrypt the exact same zero-buffer to compare
        local_c1 = cipher_clone.encrypt(zeros)
        
        if local_c1 == server_keystream:
            print(f"[+] SEED FOUND: {seed_candidate}")
            found_seed = seed_candidate
            break
    
    if found_seed is None:
        print("[-] Failed to find seed. Server might use non-time based entropy or clock skew is too large.")
        sys.exit(0)

    # 4. Decrypt the Flag
    # Since 'cipher_clone' is now synced with the server, we just continue using it.
    
    r.recvuntil(b">> ")
    r.sendline(b"2") # Option 2: Encrypt Flag
    
    r.recvuntil(b"c1 = ")
    enc_flag_hex = r.recvline().strip().decode()
    enc_flag = unhexlify(enc_flag_hex)
    
    # The server's generator has moved forward. Our local generator is also moving forward.
    # We generate the keystream for the flag's length.
    # Note: We must feed it dummy data of flag length to pump the generator
    dummy_input = b'\x00' * len(enc_flag)
    flag_keystream = cipher_clone.encrypt(dummy_input)
    
    # Decrypt: Flag = Encrypted XOR Keystream
    flag = bytes([a ^ b for a, b in zip(enc_flag, flag_keystream)])
    
    print(f"\n[SUCCESS] FLAG: {flag.decode(errors='ignore')}")
    r.close()

if __name__ == "__main__":
    solve()