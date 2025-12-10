#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void *giftcard;
char binsh[] = "/bin/sh";

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    giftcard = &giftcard;
}

void vuln() {
    char buffer[32];
    unsigned int len = 0;
     
    puts("how many bytes do you need: "); 
    scanf("%u%*c", &len);

    if (len > 0x80)
    {
        puts("nuh uh!");
        exit(1);
    }

    puts("hurry up: "); 
    read(0, buffer, len);
    __asm__ __volatile__ (
        ".intel_syntax noprefix\n" 
        "mov rax, %0\n" 
        ".att_syntax\n"
        : 
        : "r" (giftcard)
        : 
    );

    
}

void __attribute__((used)) gadget_farm() {
    __asm__ __volatile__ (
        ".intel_syntax noprefix\n"
        "pop rdi; ret\n"
        "pop rsi; ret\n"
        "pop rdx; ret\n"
        "pop rax; ret\n"
        "syscall\n"
        ".att_syntax\n"
    );
}

int main() {
    puts("Hola!");
    init();
    vuln();
    return 0;
}
