typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_404fe0;

long long _init()
{
    struct_0 **v1;  // rax

    v1 = g_404fe0;
    if (g_404fe0)
        v1 = g_404fe0();
    return v1;
}

extern unsigned long long g_404ff0;
extern unsigned long long g_404ff8;

void sub_400360()
{
    unsigned long v0;  // [bp-0x8]

    v0 = g_404ff0;
    goto g_404ff8;
}

void _start(unsigned long a0, unsigned long a1, unsigned long long a2)
{
    unsigned long long v1;  // [bp+0x0]
    unsigned long v2;  // [bp+0x8]
    unsigned long long v3;  // rax

    v1 = v3;
    __libc_start_main(main, v1, &v2, 0, 0, a2, &v1, v1); /* do not return */
}

void sub_4004b5()
{
    [D] Unsupported jumpkind Ijk_SigTRAP at address 4195509()
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

extern unsigned long long lib;

void setup()
{
    lib = dlopen(0, 2);
    srand(1900134127);
    return;
}

extern char skibidi_buffer;
extern unsigned int skibidi_cache[4];
extern unsigned long long skibidi_index;

long long skibidi_thunker(unsigned int a0)
{
    unsigned int v0;  // [bp-0x1c]
    unsigned int v2;  // eax

    if (skibidi_index > 4069)
    {
        printf("skibidi cache is full :(");
        exit(1); /* do not return */
    }
    for (v0 = 0; v0 < skibidi_index; v0 += 2)
    {
        if (a0 == skibidi_cache[v0])
        {
            sprintf(&skibidi_buffer, "thunk_%x", skibidi_cache[1 + v0] ^ a0);
            return &skibidi_buffer;
        }
    }
    skibidi_cache[skibidi_index] = a0;
    v2 = rand();
    skibidi_cache[1 + skibidi_index] = v2;
    sprintf(&skibidi_buffer, "thunk_%x", skibidi_cache[1 + skibidi_index] ^ a0);
    skibidi_index = skibidi_index + 2;
    return &skibidi_buffer;
}

int thunk_30209661(unsigned long long a0)
{
    unsigned long long v0;  // [bp-0x10]

    v0 = a0;
    return puts("\n[-] Wrong flag. Keep trying!");
}

int thunk_12578181(unsigned long long a0)
{
    unsigned long long v0;  // [bp-0x10]

    v0 = a0;
    return puts("    You successfully reversed the flag!");
}

int thunk_9c7b8bce(unsigned long long a0)
{
    unsigned long long v0;  // [bp-0x10]

    v0 = a0;
    return puts("\n[+] Correct! Well done!");
}

long long thunk_9cdcba3e(char *a0)
{
    char *v1;  // rax

    v1 = strcspn(a0, "\n");
    *((char *)(a0 + v1)) = 0;
    return v1;
}

int thunk_bf9a04a8(unsigned long long a0)
{
    unsigned long long v0;  // [bp-0x10]

    v0 = a0;
    return puts("Error reading input!");
}

int thunk_4fc8fcf(unsigned long long a0)
{
    unsigned long long v0;  // [bp-0x10]

    v0 = a0;
    return printf("Enter the flag: ");
}

void thunk_d58f7cb7(unsigned long long a0)
{
    unsigned long long v0;  // [bp-0x10]

    v0 = a0;
    thunk_2c121ef3();
    return;
}

void thunk_f5d40b83(unsigned long long a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]

    v5 = a0;
    v4 = a1;
    v3 = a2;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    exit(1); /* do not return */
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

int thunk_f045ecda(FILE_t **a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]

    v4 = a1;
    v3 = a2;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    return fclose(*(a0));
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

long long thunk_ccaf6007(FILE_t **a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, void* a5)
{
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]

    v3 = a1;
    v2 = a2;
    v1 = a3;
    v0 = a4;
    return fread(a5, 1, 255, *(a0));
}

long long thunk_91ed0d71(unsigned long long *a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, char *a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]

    v3 = a1;
    v2 = a2;
    v1 = a3;
    v0 = a5;
    *(a0) = fopen(a4, "r");
    return a0;
}

int thunk_733e6d85(unsigned long long a0, unsigned int *a1, unsigned long long a2, unsigned long long a3, char *a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x10]

    v3 = a0;
    v2 = a2;
    v1 = a3;
    v0 = a5;
    return snprintf(a4, 0x200, "/proc/%d/cmdline", *(a1));
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

int thunk_dfe46439(FILE_t **a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]

    v4 = a1;
    v3 = a2;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    return fclose(*(a0));
}

void thunk_9c8076af(unsigned long long *a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]

    v1 = a4;
    v0 = a5;
    __isoc23_fscanf(*(a0), "%*d %s %c %d", a2, a3, a1);
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

long long thunk_bde1e15a(FILE_t **a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]

    v4 = a1;
    v3 = a2;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    *(a0) = fopen("/proc/self/stat", "r");
    return a0;
}

long long thunk_537ee40b(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned int *a4, unsigned long a5)
{
    *(a4) = 0;
    return a4;
}

typedef struct struct_0 {
    char padding_0[40];
    unsigned long long field_28;
} struct_0;

long long thunk_7c444269(unsigned long a0, unsigned long a1, unsigned long a2, struct_0 *a3, unsigned long a4, unsigned long a5)
{
    a3->field_28 = 9082954382513926454;
    return &a3->field_28;
}

typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long thunk_8fcfc1a9(unsigned long a0, unsigned long a1, unsigned long a2, struct_0 *a3, unsigned long a4, unsigned long a5)
{
    a3->field_20 = 15513938451059110358;
    return &a3->field_20;
}

typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long thunk_a8cd2ab6(unsigned long a0, unsigned long a1, unsigned long a2, struct_0 *a3, unsigned long a4, unsigned long a5)
{
    a3->field_18 = 9112335326098593919;
    return &a3->field_18;
}

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long thunk_ed211175(unsigned long a0, unsigned long a1, unsigned long a2, struct_0 *a3, unsigned long a4, unsigned long a5)
{
    a3->field_10 = 4469141452009139530;
    return &a3->field_10;
}

typedef struct struct_0 {
    char padding_0[8];
    unsigned long long field_8;
} struct_0;

long long thunk_b618cce9(unsigned long a0, unsigned long a1, unsigned long a2, struct_0 *a3, unsigned long a4, unsigned long a5)
{
    a3->field_8 = 7140607323783137869;
    return &a3->field_8;
}

long long thunk_4dd7fda5(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long long *a3, unsigned long a4, unsigned long a5)
{
    *(a3) = 17646779789530123288;
    return a3;
}

void thunk_3fef8767(unsigned int *a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x18]

    v3 = a1;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    thunk_7de26323(a2, *(a0));
    return;
}

void thunk_3d1fe6cf(unsigned int *a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long *a5)
{
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x18]

    v2 = a1;
    v1 = a3;
    v0 = a4;
    thunk_ba9ca5f4(*(a5), a2, *(a0));
    return;
}

long long thunk_4ff37435(unsigned int *a0, unsigned int *a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long *a5)
{
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v4;  // rax

    v2 = a2;
    v1 = a3;
    v0 = a4;
    v4 = thunk_3d7f35a6(*(a5), *(a0));
    *(a1) = v4;
    return v4;
}

int thunk_1a8576aa(unsigned long long a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]

    v5 = a0;
    v4 = a1;
    v3 = a2;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    return puts("Flag must end with '}'");
}

int thunk_e4dcaef(unsigned long long a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]

    v5 = a0;
    v4 = a1;
    v3 = a2;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    return puts("Flag must start with 'AKASEC{'");
}

int thunk_71c9ff75(unsigned long long a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, unsigned long long a5)
{
    unsigned long long v0;  // [bp-0x38]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]

    v5 = a0;
    v4 = a1;
    v3 = a2;
    v2 = a3;
    v1 = a4;
    v0 = a5;
    return printf("Wrong length! Expected %d characters.\n", 48);
}

long long thunk_63ad0d4a(unsigned int *a0, unsigned long long a1, unsigned long long a2, unsigned long long a3, unsigned long long a4, char **a5)
{
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]

    v3 = a1;
    v2 = a2;
    v1 = a3;
    v0 = a4;
    *(a0) = strlen(*(a5));
    return a0;
}

long long thunk_5667b8fe(unsigned int *a0, unsigned long long *a1, unsigned long a2)
{
    unsigned long long v1;  // rdx
    unsigned long v2;  // rax

    v1 = *(a1);
    v2 = *(a0);
    *((char *)(v2 + v1)) = *((char *)(*(a0) + *(a1))) ^ *((char *)(*(a0) - 1 + *(a1)));
    return v2 + v1;
}

long long thunk_6a0c458(unsigned int *a0, unsigned long a1, unsigned long a2)
{
    *(a0) = 1;
    return a0;
}

long long thunk_13a11be9(unsigned int *a0, char *a1, unsigned long a2, unsigned long long *a3, unsigned long a4)
{
    unsigned long v1;  // rax

    v1 = *(a1);
    *((char *)(*(a3) + *(a0))) = v1;
    return v1;
}

long long thunk_8146f783(unsigned int *a0, char *a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a1) = (char)*(a0) ^ *(a1);
    return a1;
}

long long thunk_f49b6b4b(unsigned int *a0, char *a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a1) = *(a1) + (char)*(a0) * 13;
    return a1;
}

long long thunk_2f731ec9(unsigned long a0, char *a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a1) = *(a1) >> 5 | *(a1) * 8;
    return a1;
}

long long thunk_7d676f54(unsigned long a0, char *a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a1) = *(a1) ^ 66;
    return a1;
}

long long thunk_fec282a5(unsigned int *a0, char *a1, unsigned long long *a2, unsigned long a3, unsigned long a4)
{
    *(a1) = *((char *)(*(a0) + *(a2)));
    return a1;
}

long long thunk_78c5a08c(unsigned int *a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a0) = 0;
    return a0;
}

long long thunk_3daaee0b(unsigned int *a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a0) = *(a0) ^ 3735928559;
    return a0;
}

long long thunk_6adc8c29(unsigned int *a0, unsigned int *a1, unsigned int *a2, unsigned long a3, unsigned long a4)
{
    *(a0) = *(a0) + (*(a2) + 1) * *(a1);
    return a0;
}

long long thunk_10cd3c19(unsigned int *a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a0) = __ROL__(*(a0), 7);
    return a0;
}

long long thunk_b05e5dbd(unsigned int *a0, unsigned int *a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a0) = *(a0) ^ *(a1);
    return a0;
}

long long thunk_97855e8a(unsigned long a0, unsigned int *a1, unsigned int *a2, unsigned long long *a3, unsigned long a4)
{
    *(a1) = *((char *)(*(a2) + *(a3)));
    return a1;
}

long long thunk_6647ca54(unsigned long a0, unsigned long a1, unsigned int *a2, unsigned long a3, unsigned long a4)
{
    *(a2) = 0;
    return a2;
}

long long thunk_725adc05(unsigned int *a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    *(a0) = 305419896;
    return a0;
}

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

typedef struct struct_3 {
    struct struct_3 *field_0;
} struct_3;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

typedef struct struct_6 {
    struct struct_6 *field_0;
} struct_6;

typedef struct struct_5 {
    struct struct_5 *field_0;
} struct_5;

typedef struct struct_2 {
    struct struct_2 *field_0;
} struct_2;

extern unsigned long long lib;

long long thunk_3d7f35a6(unsigned long long a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x24]
    unsigned long long v1;  // [bp-0x20]
    char v2;  // [bp-0x14], Other Possible Types: unsigned int
    char v3;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned long long v7;  // rax
    struct_0 **v8;  // rax
    unsigned long long v9;  // rax
    struct_3 **v10;  // rax
    unsigned long long v11;  // rax
    struct_4 **v12;  // rax
    unsigned long long v13;  // rax
    struct_1 **v14;  // rax
    unsigned long long v15;  // rax
    struct_6 **v16;  // rax
    unsigned long long v17;  // rax
    struct_5 **v18;  // rax
    unsigned long long v19;  // rax
    struct_2 **v20;  // rax

    v1 = a0;
    v0 = a1;
    v7 = skibidi_thunker(1104696647);
    v8 = dlsym(lib, v7, v7);
    v8(&v2, &v3, &v5, &v1, &v0, v8);
    v9 = skibidi_thunker(210895903);
    v10 = dlsym(lib, v9, v9);
    v10(&v2, &v3, &v5, &v1, &v0, v10);
    for (; v5 < v0; v5 += 1)
    {
        v11 = skibidi_thunker(2865906717);
        v12 = dlsym(lib, v11, v11);
        v12(&v2, &v3, &v5, &v1, &v0, v12);
        v13 = skibidi_thunker(2739504163);
        v14 = dlsym(lib, v13, v13);
        v14(&v2, &v3, &v5, &v1, &v0, v14);
        v15 = skibidi_thunker(582996692);
        v16 = dlsym(lib, v15, v15);
        v16(&v2, &v3, &v5, &v1, &v0, v16);
        v17 = skibidi_thunker(2121848602);
        v18 = dlsym(lib, v17, v17);
        v18(&v2, &v3, &v5, &v1, &v0, v18);
        v19 = skibidi_thunker(1800436767);
        v20 = dlsym(lib, v19, v19);
        v20(&v2, &v3, &v5, &v1, &v0, v20);
    }
    return v2;
}

typedef struct struct_5 {
    struct struct_5 *field_0;
} struct_5;

typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

typedef struct struct_6 {
    struct struct_6 *field_0;
} struct_6;

typedef struct struct_3 {
    struct struct_3 *field_0;
} struct_3;

typedef struct struct_2 {
    struct struct_2 *field_0;
} struct_2;

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

extern unsigned long long lib;

void thunk_ba9ca5f4(unsigned long long a0, unsigned long long a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x2c]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned int v4;  // [bp-0x10]
    char v5;  // [bp-0x9]
    unsigned long long v7;  // rax
    struct_5 **v8;  // rax
    unsigned long long v9;  // rax
    struct_1 **v10;  // rax
    unsigned long long v11;  // rax
    struct_6 **v12;  // rax
    unsigned long long v13;  // rax
    struct_3 **v14;  // rax
    unsigned long long v15;  // rax
    struct_2 **v16;  // rax
    unsigned long long v17;  // rax
    struct_0 **v18;  // rax
    unsigned long long v19;  // rax
    struct_4 **v20;  // rax

    v2 = a0;
    v1 = a1;
    v0 = a2;
    v7 = skibidi_thunker(926837014);
    v8 = dlsym(lib, v7, v7);
    v8(&v4, &v5, &v2, &v1, &v0, v8);
    for (; v4 < v0; v4 += 1)
    {
        v9 = skibidi_thunker(4169661203);
        v10 = dlsym(lib, v9, v9);
        v10(&v4, &v5, &v2, &v1, &v0, v10);
        v11 = skibidi_thunker(401015899);
        v12 = dlsym(lib, v11, v11);
        v12(&v4, &v5, &v2, &v1, &v0, v12);
        v13 = skibidi_thunker(1683597001);
        v14 = dlsym(lib, v13, v13);
        v14(&v4, &v5, &v2, &v1, &v0, v14);
        v15 = skibidi_thunker(3633749383);
        v16 = dlsym(lib, v15, v15);
        v16(&v4, &v5, &v2, &v1, &v0, v16);
        v17 = skibidi_thunker(4081026679);
        v18 = dlsym(lib, v17, v17);
        v18(&v4, &v5, &v2, &v1, &v0, v18);
        v19 = skibidi_thunker(1028229118);
        v20 = dlsym(lib, v19, v19);
        v20(&v4, &v5, &v2, &v1, &v0, v20);
    }
    return;
}

typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern unsigned long long lib;

void thunk_7de26323(unsigned long long a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x24]
    unsigned long long v1;  // [bp-0x20]
    unsigned int v3;  // [bp-0xc]
    unsigned long long v5;  // rax
    struct_1 **v6;  // rax
    unsigned long long v7;  // rax
    struct_0 **v8;  // rax

    v1 = a0;
    v0 = a1;
    v5 = skibidi_thunker(880551664);
    v6 = dlsym(lib, v5, v5);
    v6(&v3, &v1, &v0, &v1, v6);
    for (; v3 < v0; v3 += 1)
    {
        v7 = skibidi_thunker(681662581);
        v8 = dlsym(lib, v7, v7);
        v8(&v3, &v1, &v0, &v1, v8);
    }
    return;
}

typedef struct struct_13 {
    struct struct_13 *field_0;
} struct_13;

typedef struct struct_11 {
    struct struct_11 *field_0;
} struct_11;

typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

typedef struct struct_6 {
    struct struct_6 *field_0;
} struct_6;

typedef struct struct_9 {
    struct struct_9 *field_0;
} struct_9;

typedef struct struct_10 {
    struct struct_10 *field_0;
} struct_10;

typedef struct struct_12 {
    struct struct_12 *field_0;
} struct_12;

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

typedef struct struct_2 {
    struct struct_2 *field_0;
} struct_2;

typedef struct struct_3 {
    struct struct_3 *field_0;
} struct_3;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

typedef struct struct_5 {
    struct struct_5 *field_0;
} struct_5;

typedef struct struct_7 {
    struct struct_7 *field_0;
} struct_7;

typedef struct struct_8 {
    struct struct_8 *field_0;
} struct_8;

extern unsigned long long lib;

long long validate_flag(char *a0)
{
    char *v0;  // [bp-0x90]
    char v1;  // [bp-0x80], Other Possible Types: unsigned int
    char v2;  // [bp-0x7c], Other Possible Types: unsigned int
    char v3;  // [bp-0x78]
    char v4;  // [bp-0x48]
    char v5;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned long long v7;  // rax
    unsigned long long v9;  // rax
    unsigned long long v11;  // rax
    unsigned long long v13;  // rax
    unsigned long long v15;  // rax
    unsigned long long v17;  // rax
    unsigned long long v19;  // rax
    unsigned long long v21;  // rax
    unsigned long long v23;  // rax
    unsigned long long v25;  // rax
    unsigned long long v27;  // rax
    unsigned long long v29;  // rax
    unsigned long long v31;  // rax
    unsigned long long v33;  // rax

    v0 = a0;
    v7 = skibidi_thunker(286737328);
    dlsym(lib, v7, v7)(&v1, &v2, &v3, &v4, &v5, &v0);
    if (v1 != 48)
    {
        v9 = skibidi_thunker(1681994494);
        dlsym(lib, v9, v9)(&v1, &v2, &v3, &v4, &v5, &v0);
        return 0;
    }
    else if (strncmp(v0, "AKASEC{", 7))
    {
        v11 = skibidi_thunker(465897316);
        dlsym(lib, v11, v11)(&v1, &v2, &v3, &v4, &v5, &v0);
        return 0;
    }
    else if (v0[1 + v1] != 125)
    {
        v13 = skibidi_thunker(252558113);
        dlsym(lib, v13, v13)(&v1, &v2, &v3, &v4, &v5, &v0);
        return 0;
    }
    else
    {
        v15 = skibidi_thunker(1518057918);
        dlsym(lib, v15, v15)(&v1, &v2, &v3, &v4, &v5, &v0);
        if (v2 != 1278831676)
            return 0;
        v17 = skibidi_thunker(1125850280);
        dlsym(lib, v17, v17)(&v1, &v2, &v3, &v4, &v5, &v0);
        v19 = skibidi_thunker(1643649155);
        dlsym(lib, v19, v19)(&v1, &v2, &v3, &v4, &v5, &v0);
        v21 = skibidi_thunker(634659419);
        dlsym(lib, v21, v21)(&v1, &v2, &v3, &v4, &v5, &v0);
        v23 = skibidi_thunker(3917304307);
        dlsym(lib, v23, v23)(&v1, &v2, &v3, &v4, &v5, &v0);
        v25 = skibidi_thunker(2180505403);
        dlsym(lib, v25, v25)(&v1, &v2, &v3, &v4, &v5, &v0);
        v27 = skibidi_thunker(4221920192);
        dlsym(lib, v27, v27)(&v1, &v2, &v3, &v4, &v5, &v0);
        v29 = skibidi_thunker(2835775014);
        dlsym(lib, v29, v29)(&v1, &v2, &v3, &v4, &v5, &v0);
        v31 = skibidi_thunker(1430913233);
        dlsym(lib, v31, v31)(&v1, &v2, &v3, &v4, &v5, &v0);
        v33 = skibidi_thunker(828125570);
        dlsym(lib, v33, v33)(&v1, &v2, &v3, &v4, &v5, &v0);
        for (; v5 < v1; v5 += 1)
        {
            if ((&v3)[v5] != (&v4)[v5])
                return 0;
        }
        return 1;
    }
}

typedef struct struct_6 {
    struct struct_6 *field_0;
} struct_6;

typedef struct struct_7 {
    struct struct_7 *field_0;
} struct_7;

typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

typedef struct struct_2 {
    struct struct_2 *field_0;
} struct_2;

typedef struct struct_3 {
    struct struct_3 *field_0;
} struct_3;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

typedef struct struct_5 {
    struct struct_5 *field_0;
} struct_5;

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern unsigned long long lib;

void thunk_2c121ef3()
{
    char v0;  // [bp-0x428]
    char v1;  // [bp-0x41c]
    char v2;  // [bp-0x418]
    char v3;  // [bp-0x309]
    char v4;  // [bp-0x308]
    char v5[256];  // [bp-0x108]
    unsigned long long v7;  // rax
    unsigned long long v9;  // rax
    unsigned long long v11;  // rax
    unsigned long long v13;  // rax
    unsigned long long v15;  // rax
    unsigned long long v17;  // rax
    unsigned long long v19;  // rax
    unsigned long long v21;  // rax

    v7 = skibidi_thunker(3555593369);
    dlsym(lib, v7, v7)(&v0, &v1, &v2, &v3, &v4, &v5);
    if (!*((long long *)&v0))
        return;
    v9 = skibidi_thunker(4158922712);
    dlsym(lib, v9, v9)(&v0, &v1, &v2, &v3, &v4, &v5);
    v11 = skibidi_thunker(2558543436);
    dlsym(lib, v11, v11)(&v0, &v1, &v2, &v3, &v4, &v5);
    v13 = skibidi_thunker(1325996527);
    dlsym(lib, v13, v13)(&v0, &v1, &v2, &v3, &v4, &v5);
    v15 = skibidi_thunker(2673312098);
    dlsym(lib, v15, v15)(&v0, &v1, &v2, &v3, &v4, &v5);
    if (!*((long long *)&v0))
        return;
    v17 = skibidi_thunker(3903557165);
    dlsym(lib, v17, v17)(&v0, &v1, &v2, &v3, &v4, &v5);
    v19 = skibidi_thunker(2985371398);
    dlsym(lib, v19, v19)(&v0, &v1, &v2, &v3, &v4, &v5);
    if (strstr(&v5, "gdb") || strstr(&v5, "lldb") || strstr(&v5, "radare") || strstr(&v5, "r2") || strstr(&v5, "edb") || strstr(&v5, "ida"))
    {
        v21 = skibidi_thunker(3404066228);
        dlsym(lib, v21, v21)(&v0, &v1, &v2, &v3, &v4, &v5);
    }
    return;
}

typedef struct struct_5 {
    struct struct_5 *field_0;
} struct_5;

typedef struct struct_2 {
    struct struct_2 *field_0;
} struct_2;

typedef struct struct_6 {
    struct struct_6 *field_0;
} struct_6;

typedef struct struct_3 {
    struct struct_3 *field_0;
} struct_3;

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

extern FILE_t *__bss_start;
extern unsigned long long lib;

int main()
{
    char v0[256];  // [bp-0x108]
    unsigned long long v2;  // rax
    unsigned long long v4;  // rax
    unsigned long long v6;  // rax
    unsigned long long v8;  // rax
    unsigned long long v10;  // rax
    unsigned long long v12;  // rax
    unsigned long long v14;  // rax

    v2 = skibidi_thunker(4178036421);
    dlsym(lib, v2, v2)(&v0);
    v4 = skibidi_thunker(1003317752);
    dlsym(lib, v4, v4)(&v0);
    if (!fgets(&v0, 0x100, __bss_start))
    {
        v6 = skibidi_thunker(2468285464);
        dlsym(lib, v6, v6)(&v0);
        return 1;
    }
    v8 = skibidi_thunker(2958668430);
    dlsym(lib, v8, v8)(&v0);
    if ((int)validate_flag(&v0))
    {
        v10 = skibidi_thunker(3602196087);
        dlsym(lib, v10, v10)(&v0);
        v12 = skibidi_thunker(2023001877);
        dlsym(lib, v12, v12)(&v0);
    }
    else
    {
        v14 = skibidi_thunker(60956451);
        dlsym(lib, v14, v14)(&v0);
    }
    return 0;
}

void _fini()
{
    return;
}

