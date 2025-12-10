from pwn import *
from Crypto.Util.strxor import strxor

strr = b"./flag.txt" 
key = 10 * b'\x1b'

print(f"str {strr.hex()}")
print(f"str {key.hex()}")
print(f"str {strxor(key, strr)}")