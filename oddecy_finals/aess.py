from binascii import unhexlify
import random
import sys
import string

# --- YOUR CAPTURED DATA ---
# Keystream verification (dddd -> d786)
TARGET_KEYSTREAM = [0x0a, 0x5b]
# The Encrypted Flag
FLAG_ENC_HEX = "a1b5c7374dbedf86dc492b25e9e5b5bf690c2d8302f2c7318ac0a3323efddff32be58bdf540d835de1d61d03fd"
ENC_FLAG_BYTES = unhexlify(FLAG_ENC_HEX)

def is_readable_flag(text_bytes):
    """Returns True if the text looks like a valid flag."""
    # Check for flag format
    if b"CO{" in text_bytes or b"flag{" in text_bytes:
        return True
    
    # Or check if it's mostly readable ASCII (letters/numbers)
    printable_chars = set(string.printable.encode())
    match_count = sum(1 for b in text_bytes if b in printable_chars)
    
    # If 95% of characters are readable, it's the flag
    return match_count > (len(text_bytes) * 0.95)

def solve():
    print("[*] Starting Deep Scan (Ignoring False Positives)...")
    
    # We scan a large range to be safe
    for i in range(1000000):
        random.seed(i)
        
        # --- 1. Inline Simulation (Fast Check) ---
        state = random.getrandbits(64)
        
        # Byte 1 check
        b1 = 0
        while b1 == 0:
            for _ in range(8):
                tap = random.randint(1, 63)
                fb = ((state >> 13) ^ (state >> 37) ^ (state >> tap)) & 1
                state = (state >> 1) | (fb << 63)
                b1 = (b1 << 1) | (state & 1)
        if b1 != TARGET_KEYSTREAM[0]: continue

        # Byte 2 check
        b2 = 0
        while b2 == 0:
            for _ in range(8):
                tap = random.randint(1, 63)
                fb = ((state >> 13) ^ (state >> 37) ^ (state >> tap)) & 1
                state = (state >> 1) | (fb << 63)
                b2 = (b2 << 1) | (state & 1)
        if b2 != TARGET_KEYSTREAM[1]: continue
        
        # --- 2. MATCH FOUND -> Decrypt Flag to Verify ---
        # The state is already advanced by 2 bytes (consumed above).
        # This matches your flow (Encrypted 2 bytes 'dddd' -> Then Flag)
        
        # We need to simulate the cipher class properly for the flag length
        # We continue using the current 'state' variable
        
        flag_candidate = b""
        temp_state = state # Copy state so we don't mess up loop if needed
        
        valid_decrypt = True
        
        for byte_enc in ENC_FLAG_BYTES:
            k = 0
            while k == 0:
                for _ in range(8):
                    tap = random.randint(1, 63)
                    fb = ((temp_state >> 13) ^ (temp_state >> 37) ^ (temp_state >> tap)) & 1
                    temp_state = (temp_state >> 1) | (fb << 63)
                    k = (k << 1) | (temp_state & 1)
            
            flag_candidate += bytes([byte_enc ^ k])

        # --- 3. VALIDATE TEXT ---
        if is_readable_flag(flag_candidate):
            print(f"\n\n[!!!] REAL FLAG FOUND at PID: {i}")
            print(f"[SUCCESS] {flag_candidate.decode(errors='ignore')}")
            sys.exit(0)
        else:
            # It was a false positive (like PID 21207)
            # Just print a dot and continue
            sys.stdout.write(".") 
            sys.stdout.flush()

        if i % 50000 == 0:
            sys.stdout.write(f"\rScanning {i}...")

if __name__ == "__main__":
    solve()