from pwn import *
from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import pad
import base64, json

p = process(['python', 'chall.py'])
iv = ''

def do_partial_padding_oracle_atack(lwl, data):
    passwd = b''
    # print(data)
    while len(passwd) < 9:

        for chrr in range(0, 256):
            chr = chrr.to_bytes(1)
            # print( f"trying.    {chr}")
            s1 = b'\x00' * (9 - len(passwd) - 1) + chr + passwd + 7 * b'\x07'
            zero = strxor(s1, bytes.fromhex(data[:32]))
            
            s2 = b'\x00' * (9 - len(passwd) - 1) + (7 + len(passwd) + 1) * (7 + len(passwd) + 1).to_bytes(1)
            # print(s2)
            to_send = strxor(zero, s2)
            # print("TASK: " + s3.hex() + data[32:])
            payload = "TASK: " + lwl + to_send.hex() + data[32:]
            # print(payload)
            p.sendline(payload.encode())
            line = p.recv(timeout=2).decode()
            # print(line)
            if line[:6] != 'Error:' and line[:6] != 'The pa' :
                # print('boom')
                passwd = chr + passwd
                # print(passwd)
                # input()
                break
            if chr == b'\xff':
                print("tffoooooo...")
                return 
                break
            # sleep(0.1)
    print(passwd)
    return passwd


def dycrept_block(data):
    print(data)
    print(len(data))
    input()
    passwd = b''
    while len(passwd) < 16:

        for chrr in range(5, 256):
            chr = chrr.to_bytes(1)
            print( f"trying.    {chr}")
            s1 = b'\x00' * (16 - len(passwd) - 1) + chr + passwd 
            print(len(s1))
            print(s1)
            print(len(bytes.fromhex(data)))
            zero = strxor(s1, bytes.fromhex(data[:32]))
            
            s2 = b'\x00' * (16 - len(passwd) - 1) + ( len(passwd) +1) * (len(passwd) + 1).to_bytes(1)
            print(len(s2))
            print(len(zero))
            print(s2)
            to_send = strxor(zero, s2)
            # print("TASK: " + s3.hex() + data[32:])
            payload = "TASK: " + to_send.hex() + data[32:64] 
            print(payload)
            p.sendline(payload.encode())
            line = p.recv(timeout=2).decode()
            print(line)
            if line[:6] != 'Error:' and line[:6] != 'The pa' :
                print('boom')
                passwd = chr + passwd
                print(passwd)
                # input()
                break
            if chr == b'\xff':
                print(passwd)
                print("tffoooooo...")
                exit(1)
                break
            # sleep(0.1)
    print(passwd)
    return passwd
    # input()


def do_multi_padding_oracle_atack(dataa):
    print(len(dataa)/32)
    sys.exit(1)
    flag = b''
    i = 1
    # print('TASK: ' + dataa)
    while i < 7:
        if i == 6:
            flag = flag + do_partial_padding_oracle_atack(dataa[:96], dataa[96:])
        else:
            print(dataa)
            x = i - 1
            flag =  flag +  dycrept_block(dataa[((i -1) * 32):((i -1) * 32) + 64]) 
            print(flag)
            input()
        # elif (i != 1 and i != 5):
        #     falg = flag + dycrept_block(dataa[(i - 1) * 16:((i - 1) * 16 +  64)], dataa[:(i - 1) * 16], dataa[((i - 1) * 16 +  64):])
        # elif i == 0:
        #     dycrept_block(dataa[(i - 1) * 16:((i - 1) * 16 +  64)], b'', dataa[((i - 1) * 16 +  64):])
        # elif i == 5:
        #     flag = flag + dycrept_block(dataa[(i - 1) * 16:((i - 1) * 16 +  64)], dataa[:(i - 1) * 16], b'')
        i+=1
    print(flag)


def create_acc():
    p.sendline(b'2')
    p.sendline(b'123')
    p.sendline(b'123')
def login():
    p.sendline(b'1')
    p.sendline(b'123')
    p.sendline(b'123')

def make_acheq():
    p.sendline(b'1')
    p.sendline(b'1001')
    p.sendline(b'2')
    res = p.recvline_contains(b'Cheque token: ').decode().split(': ')[-1]
    return res
import ast

if __name__ == "__main__":
    create_acc()
    login()
    token = make_acheq()
    token = base64.b64decode(token).decode()
    print(type(token))
    token_fixed = token.replace("'", '"')
    data = json.loads(token_fixed)
    iv = data['iv']
    enc_cheque = data['enc_cheque']
    # iv = token[]
    print(token)
    do_multi_padding_oracle_atack(iv+enc_cheque)