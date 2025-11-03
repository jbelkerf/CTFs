typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_403fe0;

long long _init()
{
    struct_0 **v1;  // rax

    v1 = g_403fe0;
    if (g_403fe0)
        v1 = g_403fe0();
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

void sub_401141()
{
    [D] Unsupported jumpkind Ijk_SigTRAP at address 4198721()
}

void _dl_relocate_static_pie()
{
    return;
}

void deregister_tm_clones()
{
    return;
}

void register_tm_clones()
{
    return;
}

extern char completed.0;

void __do_global_dtors_aux()
{
    if (!completed.0)
    {
        deregister_tm_clones();
        completed.0 = 1;
    }
    return;
}

void frame_dummy()
{
    register_tm_clones();
    return;
}

typedef struct FILE_t {
    unsigned int _flags;
    char padding_4[4];
    char * _IO_read_ptr;
    char * _IO_read_end;
    char * _IO_read_base;
    char * _IO_write_base;
    char * _IO_write_ptr;
    char * _IO_write_end;
    char * _IO_buf_base;
    char * _IO_buf_end;
    char * _IO_save_base;
    char * _IO_backup_base;
    char * _IO_save_end;
    struct _IO_marker *_markers;
    struct _IO_FILE * _chain;
    unsigned int _fileno;
    unsigned int _flags2;
    unsigned int _old_offset;
    char padding_7c[4];
    unsigned short _cur_column;
    char _vtable_offset;
    char _shortbuf[1];
    char padding_84[4];
    struct pthread_mutex_t *_lock;
    unsigned long long _offset;
    struct _IO_codecvt * _codecvt;
    struct _IO_wide_data * _wide_data;
    struct _IO_FILE * _freeres_list;
    char __pad5;
    char padding_b1[7];
    unsigned int _mode;
    char _unused2[20];
} FILE_t;

typedef struct _IO_marker {
    struct _IO_marker * _next;
    FILE * _sbuf;
    unsigned int _pos;
} _IO_marker;

typedef struct _IO_FILE {
} _IO_FILE;

typedef struct pthread_mutex_t {
} pthread_mutex_t;

typedef struct _IO_codecvt {
    _IO_iconv_t __cd_out;
} _IO_codecvt;

typedef struct _IO_wide_data {
    wchar_t * _IO_read_ptr;
    wchar_t * _IO_read_end;
    wchar_t * _IO_read_base;
    wchar_t * _IO_write_base;
    wchar_t * _IO_write_ptr;
    wchar_t * _IO_write_end;
    wchar_t * _IO_buf_base;
    wchar_t * _IO_buf_end;
    wchar_t * _IO_save_base;
    wchar_t * _IO_backup_base;
    wchar_t * _IO_save_end;
    __mbstate_t _IO_state;
    char padding_5d[3];
    __mbstate_t _IO_last_state;
    char padding_65[3];
    unsigned short _shortbuf[1];
    _IO_jump_t _wide_vtable;
} _IO_wide_data;

typedef struct FILE {
} FILE;

typedef struct _IO_iconv_t {
} _IO_iconv_t;

typedef struct __mbstate_t {
    unsigned int __count;
    char __value;
} __mbstate_t;

typedef struct _IO_jump_t {
} _IO_jump_t;

extern FILE_t *stderr@GLIBC_2.2.5;

void read_log()
{
    int v0;  // [bp-0x98]
    unsigned int v1;  // [bp-0x84]
    FILE_t *v2;  // [bp-0x80]
    char v3;  // [bp-0x78]
    int v5;  // xmm0

    v2 = fopen("log.txt", "r");
    if (!v2)
    {
        fwrite("Something went wrong opening the file, please report to maintainer.", 1, 67, stderr@GLIBC_2.2.5);
        exit(1); /* do not return */
    }
    v1 = fread(&v3, 1, 100, v2);
    if (v1 > 0)
    {
        v0 = v5;
        puts(&v3);
        exit(0); /* do not return */
    }
    fwrite("Something went wrong reading the file, please report to maintainer.", 1, 67, stderr@GLIBC_2.2.5);
    exit(1); /* do not return */
}

void timeout_handler(unsigned int a0)
{
    unsigned int v0;  // [bp-0x1c]
    void* v1;  // [bp-0x10]

    v0 = a0;
    v1 = "DM: The demigod vaporized your party for stalling.\n";
    write(1, "DM: The demigod vaporized your party for stalling.\n", 51);
    _exit(1); /* do not return */
}

typedef struct sigaction {
} sigaction;

extern FILE_t *stderr@GLIBC_2.2.5;
extern FILE_t *stdin@GLIBC_2.2.5;
extern FILE_t *stdout@GLIBC_2.2.5;

void setup()
{
    sigaction v0;  // [bp-0xa8], Other Possible Types: unsigned long long
    unsigned long long v2;  // rcx
    void* *v3;  // rdi

    setbuf(stdin@GLIBC_2.2.5, NULL);
    setbuf(stdout@GLIBC_2.2.5, NULL);
    setbuf(stderr@GLIBC_2.2.5, NULL);
    v2 = 19;
    for (v3 = &v0; v2; v3 += 1)
    {
        v2 -= 1;
        *(v3) = 0;
    }
    v0 = timeout_handler;
    sigaction(14, &v0, NULL);
    return;
}

void cleaner()
{
    char v0;  // [bp-0x108]

    memset(&v0, 0, 0x100);
    return;
}

extern unsigned long long dm_secret;
extern FILE_t *stdin@GLIBC_2.2.5;

void encounter()
{
    char v0[32];  // [bp-0x28]
    char v1;  // [bp+0x0]

    dm_secret = *((long long *)&v1);
    puts("DM: Your party stumbles upon an angry demigod.");
    puts("DM: You have 10 seconds to do something that gets your party out alive");
    printf("You do: ");
    alarm(10);
    fgets(&v0, 80, stdin@GLIBC_2.2.5);
    alarm(0);
    if (*((long long *)&v1) == dm_secret)
        return;
    puts("DM: The god of nature swats you for disturbing the flow of nature");
    exit(1); /* do not return */
}

void start()
{
    char v0;  // [bp-0x28]

    printf("Cleric: what should we call you? ");
    read(0, &v0, 32);
    printf("Everyone: welcome to our party %s", &v0);
    encounter();
    cleaner();
    return;
}

int main()
{
    setup();
    start();
    puts("DM: That was ineffective. The demigod casts meteor shower.");
    puts("DM: 420 total damage, auto fail saving throw.");
    puts("DM: Well... sorry not sorry, thanks for playing guys.");
    return 0;
}

void _fini()
{
    return;
}

