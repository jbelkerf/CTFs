int64_t (* const)() _init()
{
    if (!__gmon_start__)
        return __gmon_start__;
    
    return __gmon_start__();
}

int64_t sub_401020()
{
    int64_t var_8 = data_403ff0;
    /* jump -> data_403ff8 */
}

int32_t putchar(int32_t c)
{
    /* tailcall */
    return putchar(c);
}

int64_t sub_401036()
{
    int64_t var_8 = 0;
    /* tailcall */
    return sub_401020();
}

int32_t puts(char const* str)
{
    /* tailcall */
    return puts(str);
}

int64_t sub_401046()
{
    int64_t var_8 = 1;
    /* tailcall */
    return sub_401020();
}

uint64_t strlen(char const* arg1)
{
    /* tailcall */
    return strlen(arg1);
}

int64_t sub_401056()
{
    int64_t var_8 = 2;
    /* tailcall */
    return sub_401020();
}

void __stack_chk_fail() __noreturn
{
    /* tailcall */
    return __stack_chk_fail();
}

int64_t sub_401066()
{
    int64_t var_8 = 3;
    /* tailcall */
    return sub_401020();
}

int32_t printf(char const* format, ...)
{
    /* tailcall */
    return printf(format);
}

int64_t sub_401076()
{
    int64_t var_8 = 4;
    /* tailcall */
    return sub_401020();
}

uint64_t strcspn(char const* arg1, char const* arg2)
{
    /* tailcall */
    return strcspn(arg1, arg2);
}

int64_t sub_401086()
{
    int64_t var_8 = 5;
    /* tailcall */
    return sub_401020();
}

char* fgets(char* buf, int32_t n, FILE* fp)
{
    /* tailcall */
    return fgets(buf, n, fp);
}

int64_t sub_401096()
{
    int64_t var_8 = 6;
    /* tailcall */
    return sub_401020();
}

void _start(int64_t arg1, int64_t arg2, void (* arg3)()) __noreturn
{
    int64_t stack_end_1;
    int64_t stack_end = stack_end_1;
    void ubp_av;
    __libc_start_main(main, __return_addr, &ubp_av, nullptr, nullptr, arg3, &stack_end);
    /* no return */
}

void* deregister_tm_clones()
{
    return &__TMC_END__;
}

int64_t (* const)() sub_401100()
{
    return nullptr;
}

void _FINI_0()
{
    if (data_404058)
        return;
    
    if (__cxa_finalize)
        __cxa_finalize(__dso_handle);
    
    deregister_tm_clones();
    data_404058 = 1;
}

int64_t (* const)() _INIT_0()
{
    /* tailcall */
    return sub_401100();
}

int64_t print_banner()
{
    putchar(0xa);
    puts(&data_402008);
    puts(&data_402088);
    puts(&data_4020b8);
    puts(&data_4020e8);
    puts(&data_402088);
    puts(&data_402118);
    putchar(0xa);
    puts("  [*] Initializing secure transaction module...");
    puts("  [*] Loading encryption protocols...");
    puts("  [*] Connecting to ELITE banking network...");
    return putchar(0xa);
}

int64_t verify_pin(char* arg1)
{
    if (strlen(arg1) != 0x26)
        return 0;
    
    if (*arg1 * 3 - arg1[1] * 2 != 0x37)
        return 0;
    
    if (arg1[1] + arg1[2] - arg1[3] != 0x41)
        return 0;
    
    if (-((arg1[4] * 5)) + arg1[2] * arg1[3] != 0x169b)
        return 0;
    
    if (arg1[5] * 2 + arg1[6] * 3 - arg1[7] != 0x132)
        return 0;
    
    if (arg1[9] * 2 + arg1[7] - arg1[8] != 0x50)
        return 0;
    
    if (arg1[8] * arg1[9] - arg1[0xa] != 0x207c)
        return 0;
    
    if (arg1[0xb] * 2 + arg1[0xa] - arg1[0xc] != 0xbd)
        return 0;
    
    if (arg1[0xd] + arg1[0xb] * 5 - arg1[0xc] * 3 != 0x17f)
        return 0;
    
    if (arg1[0xd] + arg1[0xe] - arg1[0xf] * 2 != 0x36)
        return 0;
    
    if (arg1[0xe] * arg1[0xf] - arg1[0x10] * 3 != 0x107a)
        return 0;
    
    if ((arg1[0x11] << 2) + arg1[0x10] - arg1[0x12] != 0x1a3)
        return 0;
    
    if (arg1[0x13] * 3 + arg1[0x11] * 2 - arg1[0x12] != 0x106)
        return 0;
    
    if (arg1[0x15] + arg1[0x13] - arg1[0x14] * 2)
        return 0;
    
    if (arg1[0x14] * 3 + arg1[0x15] - arg1[0x16] * 2 != 6)
        return 0;
    
    if (arg1[0x16] + arg1[0x17] * 5 - arg1[0x18] != 0x1ec)
        return 0;
    
    if (arg1[0x17] * arg1[0x18] - (arg1[0x19] << 2) != 0xf5c)
        return 0;
    
    if (arg1[0x1b] * 3 + arg1[0x19] * 2 - arg1[0x1a] != 0x155)
        return 0;
    
    if (arg1[0x1a] + arg1[0x1b] - arg1[0x1c] * 2 != 0x67)
        return 0;
    
    if (arg1[0x1e] + (arg1[0x1c] << 2) - arg1[0x1d] * 3 != 0x6c)
        return 0;
    
    if (-((arg1[0x1f] * 5)) + arg1[0x1d] * arg1[0x1e] != 0x865)
        return 0;
    
    if (arg1[0x1f] * 2 + arg1[0x1e] - arg1[0x20] != 0x5e)
        return 0;
    
    if ((arg1[0x21] << 2) + arg1[0x1f] - arg1[0x20] != 0x11f)
        return 0;
    
    if (arg1[0x22] * 2 + arg1[0x20] * 3 - arg1[0x21] != 0x12f)
        return 0;
    
    if (arg1[0x21] * arg1[0x22] - (arg1[0x23] << 2) != 0xde0)
        return 0;
    
    if (arg1[0x23] * 2 + arg1[0x22] - arg1[0x24] != 0x58)
        return 0;
    
    if (arg1[0x25] * 3 + arg1[0x23] - arg1[0x24] != 0x16f)
        return 0;
    
    if (arg1[0x25] + arg1[0x24] * 2 != 0xed)
        return 0;
    
    if (arg1[0x1e] + *arg1 + arg1[0xa] + arg1[0x14] != 0xd7)
        return 0;
    
    if (arg1[0x23] + arg1[5] + arg1[0xf] + arg1[0x19] != 0x108)
        return 0;
    
    if (arg1[0x1f] + arg1[1] + arg1[0xb] + arg1[0x15] != 0x122)
        return 0;
    
    int32_t var_1c_1 = 0;
    int32_t var_18_1 = 0;
    
    for (int32_t i = 0; i <= 0x25; i += 2)
        var_1c_1 += arg1[i];
    
    for (int32_t i_1 = 1; i_1 <= 0x25; i_1 += 2)
        var_18_1 += arg1[i_1];
    
    if (var_1c_1 != 0x56f)
        return 0;
    
    if (var_18_1 != 0x582)
        return 0;
    
    for (int32_t i_2 = 0; i_2 <= 0x25; i_2 += 1)
    {
        if (arg1[i_2] <= 0x1f || arg1[i_2] == 0x7f)
            return 0;
    }
    
    return 1;
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    print_banner();
    puts(&data_402008);
    puts(&data_402220);
    puts(&data_402118);
    printf("\n  PIN: ");
    char buf[0x108];
    int32_t result;
    
    if (fgets(&buf, 0x100, __bss_start))
    {
        buf[strcspn(&buf, "\n")] = 0;
        puts("\n  [*] Verifying PIN against secure database...");
        printf("  [*] Running %d security checks...\n", 0x72);
        puts("  [*] Performing cryptographic validation...\n");
        
        if (!verify_pin(&buf))
        {
            puts(&data_402008);
            puts(&data_402088);
            puts(&data_4023d8);
            puts(&data_402088);
            puts(&data_402410);
            puts(&data_402440);
            puts(&data_402088);
            puts(&data_402118);
            puts("\n  [!] Notifying security team...");
            puts("  [!] Locking ATM terminal...\n");
        }
        else
        {
            puts(&data_402008);
            puts(&data_402088);
            puts(&data_402300);
            puts(&data_402088);
            puts(&data_402338);
            puts(&data_402088);
            printf(&data_402367, &buf, &data_402367);
            puts(&data_402088);
            puts(&data_402118);
            puts("\n  [*] Account balance: $1,337,420.69");
            puts("  [*] Transaction history: 42 elite operations\n");
        }
        
        result = 0;
    }
    else
    {
        puts("\n  [!] Error reading input.\n");
        result = 1;
    }
    
    *(fsbase + 0x28);
    
    if (rax == *(fsbase + 0x28))
        return result;
    
    __stack_chk_fail();
    /* no return */
}

int64_t _fini() __pure
{
    return;
}


