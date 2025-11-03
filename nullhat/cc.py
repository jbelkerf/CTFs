from pwn import process
import string
import sys
import itertools
import time

# Bytes prefix/suffix
prefix = b"ELITESEC{"
suffix = b"}"

# Use visible printable characters only (no \n, \r, \t, \x0b, \x0c)
visible = ''.join(c for c in string.printable if c not in '\r\n\t\x0b\x0c')
# If you want to include space, keep it in visible; otherwise remove it:
# visible = visible.replace(' ', '')

# number of unknown characters you want to brute-force (6 in your original)
unknown_len = 6

tries = 0
for combo in itertools.product(visible, repeat=unknown_len):
    # combo is a tuple of str chars, join to a str, then encode once
    middle = ''.join(combo).encode()

    # start a fresh process if the challenge expects one per try
    p = process('./simple')

    # send the candidate flag
    candidate = prefix + middle + suffix
    p.sendline(candidate)

    # read a line with a small timeout so the script doesn't hang indefinitely
    try:
        resp = p.recvline(timeout=1)  # adjust timeout if needed
    except Exception:
        resp = b''

    # show progress every so often
    tries += 1
    if tries % 10000 == 0:
        print(f"tried {tries} candidates... latest: {candidate.decode(errors='replace')}")
    print(resp)
    print(candidate)
    # check response (bytes)
    if b'Yes' in resp:
        print("FOUND:", candidate.decode())
        sys.exit(0)

    # close process to avoid leaking handles; keep this if you spawn each try
    p.close()

print("done, not found")

