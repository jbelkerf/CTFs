from pwn import *
from binascii import unhexlify, hexlify
import random
import sys

# --- CONFIG ---
HOST = '10.25.1.156'
PORT = 8888
# --------------

def recover_state(keystream_bytes):
    """Reconstructs the 64-bit int from the first 8 bytes."""
    recovered_state = 0
    bit_pos = 0
    for byte_val in keystream_bytes:
        for i in range(7, -1, -1):
            bit = (byte_val >> i) & 1
            recovered_state |= (bit << bit_pos)
            bit_pos += 1
    return recovered_state

class feedfront:
    def __init__(self, size):
        self.size = size
        self.state = 0
    def set_state(self, seed_val):
        random.seed(seed_val)
        self.state = random.getrandbits(self.size)
    def next_state(self):
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

    # 1. Capture Leak (We still grab it just in case)
    raw_leak_line = r.recvline().strip()
    try:
        # Evaluate to get bytes: "b'\\x...'" -> b'\x...'
        leak_bytes = eval(raw_leak_line.decode())
    except:
        leak_bytes = raw_leak_line

    print(f"[*] Leak Line (String): {raw_leak_line}")

    r.recvuntil(b">> ")

    # 2. Get Keystream to find Target State
    zeros = b'\x00' * 8
    r.sendline(b"1") 
    r.recvuntil(b"data: ")
    r.sendline(hexlify(zeros))
    
    r.recvuntil(b"c1 = ")
    c1_line = r.recvline().strip()
    server_keystream = unhexlify(c1_line)
    
    target_state = recover_state(server_keystream)
    print(f"[+] Target Internal State: {target_state}")

    # 3. DICTIONARY & STRING ATTACK
    found_seed = None
    
    # List of possible seeds
    candidates = [
        # 1. The Story Words (High Probability)
        "Tangier", "tangier", "TANGIER",
        "Khouribga", "khouribga", 
        "Khenifra", "khenifra",
        "1337", "42",
        "Ibrahim", "ibrahim",
        "0VN1", "noise", "wind", "depressed",
        "student", "freedom",
        
        # 2. The Leak as a STRING (Common CTF trick)
        # Maybe random.seed("b'\\x...'") was used instead of bytes
        raw_leak_line,                 # b"b'...'"
        raw_leak_line.decode(),        # "b'...'"
        str(leak_bytes)                # "b'...'" (python repr)
    ]
    
    print(f"[*] Testing {len(candidates)} Dictionary/String candidates...")
    
    for s in candidates:
        random.seed(s)
        if random.getrandbits(64) == target_state:
            found_seed = s
            print(f"\n[!!!] SEED FOUND: {s!r}")
            break

    # 4. PID FALLBACK (Wider range)
    if not found_seed:
        print("[-] Dictionary failed. Checking PIDs (0-500,000)...")
        # Check PIDs efficiently
        for i in range(500000):
            random.seed(i)
            if random.getrandbits(64) == target_state:
                found_seed = i
                print(f"\n[!!!] SEED FOUND (PID): {i}")
                break

    if not found_seed:
        print("[-] All checks failed. Seed is truly unknown.")
        sys.exit(0)

    # 5. DECRYPT
    print(f"[*] Syncing cipher with seed: {found_seed}")
    cipher = feedfront(64)
    cipher.set_state(found_seed)
    cipher.encrypt(b'\x00' * 8) # Advance state
    
    r.sendline(b"2") 
    r.recvuntil(b"c1 = ")
    enc_flag = unhexlify(r.recvline().strip())
    
    flag_keystream = cipher.encrypt(b'\x00' * len(enc_flag))
    flag = bytes([a ^ b for a, b in zip(enc_flag, flag_keystream)])
    
    print(f"\n[SUCCESS] FLAG: {flag.decode(errors='ignore')}\n")
    r.close()

if __name__ == "__main__":
    solve()