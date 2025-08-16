import base64
import hashlib
import os

prefix = b"nfcwgqedxybi"

def check_pow(candidate_b64):
    try:
        decoded = base64.b64decode(candidate_b64)
    except Exception:
        return False
    h = hashlib.sha256(prefix + decoded).hexdigest()
    return h.startswith("000000")

def find_pow():
    tries = 0
    while True:
        # Try random 6 bytes, adjust length if needed
        candidate_bytes = os.urandom(6)
        candidate_b64 = base64.b64encode(candidate_bytes)
        if check_pow(candidate_b64):
            print("Found proof of work:", candidate_b64.decode())
            print("Hash:", hashlib.sha256(prefix + candidate_bytes).hexdigest())
            break
        tries += 1
        if tries % 100000 == 0:
            print(f"Tries: {tries}")

if __name__ == "__main__":
    find_pow()
