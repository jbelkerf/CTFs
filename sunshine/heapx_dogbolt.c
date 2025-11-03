#include <stdlib.h>

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_403fe8;

long long sub_401000()
{
    struct_0 **v1;  // rax

    v1 = g_403fe8;
    if (g_403fe8)
        v1 = g_403fe8();
    return v1;
}

extern unsigned long long g_403f70;
extern unsigned long long g_403f78;

void sub_401020()
{
    unsigned long v0;  // [bp-0x8]

    v0 = g_403f70;
    goto g_403f78;
}

void sub_401030()
{
    void* v0;  // [bp-0x8]

    v0 = 0;
    sub_401020();
    return;
}

void sub_401040()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 1;
    sub_401020();
    return;
}

void sub_401050()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 2;
    sub_401020();
    return;
}

void sub_401060()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 3;
    sub_401020();
    return;
}

void sub_401070()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 4;
    sub_401020();
    return;
}

void sub_401080()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 5;
    sub_401020();
    return;
}

void sub_401090()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 6;
    sub_401020();
    return;
}

void sub_4010a0()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 7;
    sub_401020();
    return;
}

void sub_4010b0()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 8;
    sub_401020();
    return;
}

void sub_4010c0()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 9;
    sub_401020();
    return;
}

void sub_4010d0()
{
    unsigned long long v0;  // [bp-0x8]

    v0 = 10;
    sub_401020();
    return;
}

void _start(unsigned long a0, unsigned long a1, unsigned long long a2)
{
    unsigned long long v1;  // [bp+0x0]
    unsigned long v2;  // [bp+0x8]
    unsigned long long v3;  // rax

    v1 = v3;
    __libc_start_main(main, v1, &(char)v2, 0, 0, a2, &v1, v1); /* do not return */
}

void sub_4011c5()
{
    [D] Unsupported jumpkind Ijk_SigTRAP at address 4198853()
}

void sub_4011c6()
{
    sub_4011d0();
    return;
}


void sub_4011d0()
{
    return;
}


long long sub_4011f9()
{
    return 0;
}

extern unsigned long long g_403ff8;
extern unsigned long long g_404008;
extern char g_404048;

void sub_401240()
{
    if (g_404048)
        return;
    if (g_403ff8)
        __cxa_finalize(g_404008);
    sub_4011d0();
    g_404048 = 1;
    return;
}

void sub_401280()
{
}

typedef struct struct_0 {
    char *field_0;
} struct_0;

int sub_401289(unsigned long a0, unsigned long a1, struct_0 **a2)
{
    return system(*(a2)->field_0);
}

extern unsigned long long g_404060;
extern unsigned int g_404068;

long long create_func(unsigned int a0, unsigned int a1)
{
    void* v0;  // [bp-0x18], Other Possible Types: unsigned long

    v0 = 0;
    if (a1 > 0 && a1 <= 1279)
    {
        v0 = malloc(a1);
        if (v0)
        {
            puts("[INFO] Creating new log...");
            (&g_404060)[2 * a0] = v0;
            (&g_404068)[4 * a0] = a1;
            return 1;
        }
        return 0;
    }
    puts("[ERROR] Invalid size!!");
    return 0;
}

extern unsigned long long g_404060[4];

void read_func(unsigned int a0)
{
    if (a0 >= 0 && a0 <= 15)
    {
        if (!g_404060[2 * a0])
        {
            printf("[ERROR] Log #%d doesn't exist!!\n", a0);
            return;
        }
        printf("%s", g_404060[2 * a0]);
        return;
    }
    puts("[ERROR] Invalid log number!!");
    return;
}

extern unsigned long long g_404060[4];
extern unsigned int g_404068[4];

void write_func(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x51c]
    char v1;  // [bp-0x518]
    unsigned long long v3;  // rcx
    void* *v4;  // rdi

    v3 = 160;
    for (v4 = &v1; v3; v4 += 1)
    {
        v3 -= 1;
        *(v4) = 0;
    }
    v0 = 0;
    if (a0 >= 0 && a0 <= 15)
    {
        if (!g_404060[2 * a0])
        {
            printf("[ERROR] Log #%p doesn't exist!!\n", &g_404060[2 * a0]);
            return;
        }
        if (a1 >= 0 && a1 < g_404068[4 * a0])
        {
            printf("Enter log data: ");
            v0 = read(0, &v1, g_404068[4 * a0] - 1 - a1);
            memcpy(g_404060[2 * a0] + a1, &v1, v0 - 1);
            return;
        }
        puts("[ERROR] Write offset is invalid!!");
        return;
    }
    puts("[ERROR] Invalid log number!!");
    return;
}

extern unsigned long long g_404060[4];

void delete_func(unsigned int a0)
{
    if (a0 >= 0 && a0 <= 15)
    {
        if (!g_404060[2 * a0])
        {
            printf("[ERROR Log #%d doesn't exist!!\n", a0);
            return;
        }
        free(g_404060[2 * a0]);
        return;
    }
    puts("[ERROR] Invalid log number!!");
    return;
}

extern unsigned long long intro;
extern unsigned long long help;
extern unsigned long long g_404060[4];

int main()
{
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    void* v4;  // [bp-0x18]

    v4 = 0;
    v0 = 0;
    v1 = 0;
    v2 = 0;
    printf("%s", intro);
    while (true)
    {
        printf("> ");
        __isoc99_scanf("%8s[\n]", &v4);
        if (!strncmp(&v4, "help", 4))
        {
            printf("%s", help);
        }
        else
        {
            if (!strncmp(&v4, "exit", 4))
            {
                puts("\n[INFO] Shutting down HeapX LogUplink...");
                for (v3 = 0; v3 <= 15; v3 += 1)
                {
                    if (g_404060[2 * v3])
                        free(g_404060[2 * v3]);
                }
                return 0;
            }
            __isoc99_scanf("%d", &v0);
            if (!strncmp(&v4, "new", 3))
            {
                if ((int)create_func(v2, v0))
                {
                    puts("[OK] Successfully created Log!");
                    v2 += 1;
                    continue;
                }
            }
            else
            {
                if (!strncmp(&v4, "read", 4))
                {
                    read_func(v0);
                    continue;
                }
                else if (!strncmp(&v4, "write", 5))
                {
                    __isoc99_scanf("%d", &v1);
                    write_func(v0, v1);
                    continue;
                }
                else if (!strncmp(&v4, "delete", 6))
                {
                    delete_func(v0);
                    continue;
                }
                else
                {
                    printf("[ERROR] Invalid command option: %s\n", &v4);
                }
            }
        }
    }
}

extern FILE_t *stderr;
extern FILE_t *stdout;

long long sub_401911()
{
    unsigned long v0;  // [bp-0x10]
    unsigned long long *v2;  // fs

    setvbuf(stdout, NULL, 2, 0);
    setvbuf(stderr, NULL, 2, 0);
    return v0 - v2[5];
}

void sub_401980()
{
    return;
}

