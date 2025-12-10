from binascii import unhexlify
from Crypto.Cipher import AES
import random
from Crypto.Random import get_random_bytes

flag = open("flag.txt", 'r').read().strip().encode()
key = get_random_bytes(32)
print(key[:8])

def xor(a, b):
    data = []
    for x, y in zip(a, b):
        data.append(x ^ y)
    return bytes(data)

class CTR:
    def __init__(self):
        self.key = key
    
    def encrypt(self, data):
        nonce = get_random_bytes(8)
        cipher = AES.new(self.key, AES.MODE_CTR, nonce=nonce)
        ciphertext = cipher.encrypt(data)
        return ciphertext, nonce
    
    def decrypt(self, ciphertext, nonce):
        cipher = AES.new(self.key, AES.MODE_CTR, nonce=nonce)
        return cipher.decrypt(ciphertext)

class feedfront:
    def __init__(self, size):
        self.size = size
        self.state = random.getrandbits(size)
    def next_state(self):
        self.state = (self.state >> 1) | ((((self.state >> 13) ^ (self.state >> 37) ^ (self.state >> random.randint(1, self.size - 1))) & 1) << (self.size - 1))
    def noise(self, n):
        zeros = random.randint(0, n - 1)
        noise = [0] * zeros + [1] * (n - zeros)
        random.shuffle(noise)
        return noise
    def get_byte(self):
        b_data = 0
        while b_data == 0:
            for _ in range(8):
                lsb = self.state & 1
                b_data = (b_data << 1) | lsb
                self.next_state()
        return b_data
    def get_rand_bytes(self, size):
        data = []
        for _ in range(size):
            data.append(self.get_byte())
        return bytes(data)
    def encrypt(self, data):
        key = self.get_rand_bytes(len(data))
        return xor(data, key)

BANNER = r"""
      ___           ___           ___     
     /\  \         /\  \         /\  \    
    /::\  \        \:\  \       /::\  \   
   /:/\:\  \        \:\  \     /:/\:\  \  
  /:/  \:\  \       /::\  \   /::\~\:\  \ 
 /:/__/ \:\__\     /:/\:\__\ /:/\:\ \:\__\
 \:\  \ /:/  /    /:/  \/__/ \/__\:\/:/  /
  \:\  /:/  /    /:/  /           \::/  / 
   \:\/:/  /     \/__/             \/__/  
    \::/  /                               
     \/__/                                
"""

if __name__ == "__main__":
    print(BANNER)
    enc1 = feedfront(64)
    enc2 = CTR()
    while True:
        print("""1 - Encrypt data
2 - Encrypt flag
3 - Exit""")
        opt = int(input(">> "))
        if opt == 1:
            data = unhexlify(input("data: "))
            c1 = enc1.encrypt(data)
            print(f"c1 = {c1.hex()}")
            c2, nonce = enc2.encrypt(data)
            print(f"c2 = {nonce.hex()}:{c2.hex()}")
            c3 = xor(c1, c2)
            print(f"c3 = {c3.hex()}")
        elif opt == 2:
            c1 = enc1.encrypt(flag)
            print(f"c1 = {c1.hex()}")
            c2, nonce = enc2.encrypt(flag)
            print(f"c2 = {nonce.hex()}:{c2.hex()}")
            c3 = xor(c1, c2)
            print(f"c3 = {c3.hex()}")
        else:
            exit()