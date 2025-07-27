typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_403fd0;

long long _init()
{
    struct_0 **v1;  // rax

    v1 = g_403fd0;
    if (g_403fd0)
        v1 = g_403fd0();
    return v1;
}

extern unsigned long long g_403ff0;
extern unsigned long long g_403ff8;

void sub_401020()
{
    unsigned long v0;  // [bp-0x8]

    v0 = g_403ff0;
    goto g_403ff8;
}

void _start(unsigned long a0, unsigned long a1, unsigned long long a2)
{
    unsigned long long v1;  // [bp+0x0]
    unsigned long v2;  // [bp+0x8]
    unsigned long long v3;  // rax

    v1 = v3;
    __libc_start_main(main, v1, &(char)v2, 0, 0, a2, &v1, v1); /* do not return */
}

void sub_401101()
{
    [D] Unsupported jumpkind Ijk_SigTRAP at address 4198657()
}


void deregister_tm_clones()
{
    return;
}


void register_tm_clones()
{
    return;
}

extern unsigned long long __dso_handle;
extern char completed.0;
extern unsigned long long g_403fe0;

void __do_global_dtors_aux()
{
    if (completed.0)
        return;
    if (g_403fe0)
        __cxa_finalize(__dso_handle);
    deregister_tm_clones();
    completed.0 = 1;
    return;
}

void frame_dummy()
{
    register_tm_clones();
    return;
}

extern char username;

void setuser()
{
    puts("Welcome to the goose game.\nHere you have to guess a-priori, how many HONKS you will receive from a very angry goose.\nGodspeed.");
    printf("How shall we call you?\n> ");
    __isoc99_scanf("%64s", &username);
    return;
}

extern unsigned int nhonks;
extern char username;

char guess()
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]

    v0 = 0;
    v1 = 0;
    printf("%s\n\nso %s. how many honks?", "\n                                                        _...--. \n                                        _____......----'     .' \n                                  _..-''                   .' \n                                .'                       ./ \n                        _.--._.'                       .' | \n                     .-'                           .-.'  / \n                   .'   _.-.                     .     ' \n                 .'  .'   .'    _    .-.        / `./  : \n               .'  .'   .'  .--' `.  |    |`. |     .' \n            _.'  .'   .' `.'       `-'    / |.'   .' \n         _.'  .-'   .'     `-.            `      .' \n       .'   .'    .'          `-.._ _ _ _ .-.    : \n      /    /o _.-'               .--'   .'      | \n    .'-.__..-'                  /..    .`    / .' \n  .'   . '                       /.'/.'     /  | \n `---'                                   _.'   ' \n                                       /.'    .' \n                                        /.'/.' \n", &username);
    __isoc99_scanf("%d", &v0);
    putchar(10);
    for (v1 = 0; v1 < nhonks; v1 += 1)
    {
        printf(" HONK ");
    }
    putchar(10);
    return 0 == nhonks;
}

void highscore()
{
    char v0;  // [bp-0x178]
    char v1[31];  // [bp-0xf8]
    char v2;  // [bp-0xd9]
    char v3;  // [bp-0x78]
    char v4[56];  // [bp-0x58]
    unsigned long long v5;  // [bp-0x20]

    strncpy(v4, "wow %s you're so good. what message would you like to le", 56);
    v5 = 8367810652204791393;
    strncpy(&v5, "e to the world?", 15);
    printf("what's your name again?");
    __isoc99_scanf("%31s", &v3);
    v2 = 0;
    sprintf(&v1, &(unsigned long long)v4);
    printf(&v1);
    read(0, &v0, 0x400);
    printf("got it. bye now.");
    return;
}

extern FILE_t *__TMC_END__;
extern unsigned int nhonks;

int main(unsigned int a0, unsigned long long a1)
{
    unsigned long long v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0xc]
    unsigned int v4;  // eax

    v1 = a0;
    v0 = a1;
    setvbuf(__TMC_END__, NULL, 2, 0);
    srand(time(NULL));
    setuser();
    v4 = rand();
    nhonks = v4 - (unsigned int)((((v4 * -1274330955 >> 32) + v4 & 4294967295) >> 6 & 4294967295) - (v4 >> 31)) * 91 + 10;
    if (!guess())
    {
        puts("tough luck. THE GOOSE WINS! GET THE HONK OUT!");
        return 0;
    }
    highscore();
    return 0;
}

void _fini()
{
    return;
}

