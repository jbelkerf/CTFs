from pwn import *
import string

lwl = b"ELITESEC{"

lakher = b"}"


for i1 in string.printable:
    for i2 in string.printable:
        for i3 in string.printable:
            for i4 in string.printable:
                for i5 in string.printable:
                    for i6 in string.printable:
                            p = process('./simple')
                            p.sendline(lwl+ i1.encode() + i2.encode()+ i3.encode()+ i4.encode()+ i5.encode()+ i6.encode() + lakher)
                            resp = p.recvline()
                            print(resp.decode())
                            if b'Yes' in resp:
                                 print(lwl.decode() +  1.encode() + i2.encode()+ i3.encode()+ i4.encode()+ i5.encode()+ i6.encode() + lakher.decode())
                                 sys.exit(1)


