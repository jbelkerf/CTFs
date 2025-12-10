.global _start
.intel_syntax noprefix

_start:

write:
    mov rdi, 1
    lea rsi, [rip + binbash]
    mov rdx, 3
    mov eax, 1
    syscall

exit:
    mov eax, 60
    syscall
binbash:
    .string "ppp"


