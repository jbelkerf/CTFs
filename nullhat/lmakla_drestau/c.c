typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_403fd8;

long long sub_401000()
{
    struct_0 **v1;  // rax

    v1 = g_403fd8;
    if (g_403fd8)
        v1 = g_403fd8();
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

int sub_401127()
{
    char v1;  // [bp+0x38]
    void* v2;  // rbx
    unsigned long long *v3;  // fs
    unsigned long long v4;  // rax

    v2._M_dispose();
    if (*((long long *)&v1) != v3[5])
        __stack_chk_fail(); /* do not return */
    _Unwind_Resume(v4); /* do not return */
}

typedef struct struct_2 {
    struct struct_1 *field_0;
    char padding_8[48];
    char field_38;
    char padding_39[10];
    char field_43;
} struct_2;

typedef struct struct_1 {
    char padding_0[48];
    struct struct_0 *field_30;
} struct_1;

typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern void* _ZSt3cin;
extern void _ZSt4cout;

int main(unsigned long a0, unsigned long a1, char *a2)
{
    struct_2 *v0;  // [bp-0x50]
    char *v1;  // [bp-0x48]
    void* v2;  // [bp-0x40]
    char v3;  // [bp-0x38]
    struct_2 *v5;  // rdi
    unsigned long long v6;  // rdx
    char v7;  // cl
    unsigned int v8;  // ebp

    _ZSt4cout.char_traits<char>>("\nwhat she said ? : ", a2);
    v3 = 0;
    v1 = &v3;
    v2 = 0;
    v5 = *((long long *)(240 + (char *)&_ZSt3cin + _ZSt3cin[24]));
    if (!v5)
        v5.__throw_bad_cast(); /* do not return */
    if (v5->field_38)
    {
        v6 = v5->field_43;
    }
    else
    {
        v0 = v5;
        v5._M_widen_init();
        v7 = 32;
        v6 = 10;
        if (v0->field_0->field_30 != std::ctype<char>::do_widen)
            v6 = v0->field_0->field_30(v0, 10, 10, std::ctype<char>::do_widen);
    }
    _ZSt3cin.allocator<char>>(&v1, v6, v7);
    v8 = 1;
    if (sub_401360(v1))
    {
        sub_401490();
        v8 = 0;
    }
    v1._M_dispose();
    return v8;
}

void sub_401256()
{
    sub_401127(); /* do not return */
}

void _start(unsigned long a0, unsigned long a1, unsigned long long a2)
{
    unsigned long long v1;  // [bp+0x0]
    unsigned long v2;  // [bp+0x8]
    unsigned long long v3;  // rax

    v1 = v3;
    __libc_start_main(main, v1, &v2, 0, 0, a2, &v1, v1); /* do not return */
}

void sub_401285()
{
    [D] Unsupported jumpkind Ijk_SigTRAP at address 4199045()
}

void sub_401286()
{
    sub_401290();
    return;
}


void sub_401290()
{
    return;
}


long long sub_4012b9()
{
    return 0;
}

extern struct_0 *g_403fc0;
extern unsigned long long g_404068;
extern char g_4042b8;

void sub_401300()
{
    if (g_4042b8)
        return;
    if (g_403fc0)
        g_403fc0(g_404068);
    sub_401290();
    g_4042b8 = 1;
    return;
}

void sub_401350()
{
}

char sub_401360(char *a0)
{
    char v0[7];  // [bp-0x88]
    uint128_t v1;  // [bp-0x70]
    uint128_t v2;  // [bp-0x60]
    uint128_t v3;  // [bp-0x50]
    uint128_t v4;  // [bp-0x40]
    uint128_t v5;  // [bp-0x30]
    unsigned long long v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x18]
    char v9[17];  // rcx
    char v10[17];  // rcx
    unsigned int v11;  // eax
    int v12;  // [bp-0x81]

    v7 = 20;
    v1 = 3327582826336971941963127324716;
    v9 = &v0;
    v6 = 292057776154;
    v2 = 4278320777412034452680242888724;
    v3 = 1584563251355197908386551169052;
    v4 = 4753689751224795137155547529276;
    v5 = 1584563251133836979343122759696;
    do
    {
        v10 = &v9[1];
        v11 = *((int *)((char *)&v5 + -0x4 * &v0 + 0x4 * v9)) - 80;
        v10[15] = ...;
        v9 = v10;
    } while (&v12 != v9);
    return !strcmp(a0, &v0);
}

typedef struct struct_0 {
    char field_0[16];
    uint128_t field_10;
    uint128_t field_20;
    uint128_t field_30;
} struct_0;

typedef struct struct_3 {
    struct struct_2 *field_0;
    char padding_8[48];
    char field_38;
} struct_3;

typedef struct struct_2 {
    char padding_0[48];
    struct struct_1 *field_30;
} struct_2;

typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

extern void* _ZSt4cout;

void sub_401490()
{
    char v0[32];  // [bp-0xc8]
    char v1;  // [bp-0xa8]
    char v2;  // [bp-0xa4], Other Possible Types: uint128_t
    uint128_t v3;  // [bp-0x94]
    uint128_t v4;  // [bp-0x84]
    uint128_t v5;  // [bp-0x74]
    uint128_t v6;  // [bp-0x64]
    uint128_t v7;  // [bp-0x54]
    uint128_t v8;  // [bp-0x44]
    uint128_t v9;  // [bp-0x34]
    unsigned int v10;  // [bp-0x24]
    int v12;  // xmm6
    int v13;  // xmm7
    void* v14;  // rdx
    struct_0 *v15;  // rax
    int v16;  // xmm0
    int v17;  // xmm5
    struct_0 *v18;  // rax
    int v19;  // xmm1
    int v20;  // xmm3
    int v21;  // xmm1
    int v22;  // xmm3
    int v23;  // xmm2
    int v24;  // xmm2
    int v25;  // xmm4
    int v26;  // xmm4
    int v27;  // xmm10
    int v28;  // xmm1
    int v29;  // xmm10
    int v30;  // xmm3
    int v31;  // xmm10
    int v32;  // xmm2
    int v33;  // xmm10
    int v34;  // xmm4
    int v35;  // xmm10
    int v36;  // xmm10
    int v37;  // xmm2
    int v38;  // xmm4
    unsigned int v40;  // rcx
    struct_3 *v41;  // rbp
    void* v42;  // rdi
    char v43;  // sil

    v12 = ShrNV(340282366920938463463374607431768211455, 25);
    v13 = 4294967189 CONCAT 4294967189 CONCAT 4294967189 CONCAT 4294967189;
    v14 = &v0;
    v15 = &v2;
    v2 = 554597137747424316075196547115;
    v10 = 61;
    v3 = 9824292152561987857245701931051;
    v4 = 792281626286341508685820329999;
    v5 = 475368977336088802991915663462;
    v6 = 7209762789941752853874549457021;
    v7 = 2614529363081403605368510087291;
    v8 = 8873554201708286275310021771320;
    v9 = 2614529363302764534343219019809;
    v16 = 2164392969 CONCAT 2164392969 CONCAT 2164392969 CONCAT 2164392969;
    v17 = SarNV(v16, 31);
    do
    {
        v14 += 16;
        v18 = v15 + 1;
        v19 = AddV(v15->field_0, v13);
        v20 = AddV(v15->field_10, v13);
        v21 = SubV(0, SubV(ShlNV(AddV(ShlNV(v19, 1), v19), 2), v19));
        v22 = SubV(0, SubV(ShlNV(AddV(ShlNV(v20, 1), v20), 2), v20));
        v23 = AddV(v18->field_20, v13);
        v24 = SubV(0, SubV(ShlNV(AddV(ShlNV(v23, 1), v23), 2), v23));
        v25 = AddV(v18->field_10, v13);
        v26 = SubV(0, SubV(ShlNV(AddV(ShlNV(v25, 1), v25), 2), v25));
        v27 = ...;
        v28 = AddV(SubV(v21, SubV(ShlNV(v27, 7), v27)), v12);
        v29 = ...;
        v30 = AddV(SubV(v22, SubV(ShlNV(v29, 7), v29)), v12);
        v31 = ...;
        v32 = AddV(SubV(v24, SubV(ShlNV(v31, 7), v31)), v12);
        v33 = ...;
        v34 = AddV(SubV(v26, SubV(ShlNV(v33, 7), v33)), v12);
        v35 = ...;
        v36 = ...;
        v37 = ...;
        v38 = ...;
        v14[16] = QNarrowBinV(InterleaveLOV(InterleaveHIV(InterleaveHIV(v38, v37), InterleaveLOV(v38, v37)), InterleaveLOV(InterleaveHIV(v38, v37), InterleaveLOV(v38, v37))) & ShrNV(340282366920938463463374607431768211455, 8), InterleaveLOV(InterleaveHIV(InterleaveHIV(SubV(v30, SubV(ShlNV(v36, 7), v36)), SubV(v28, SubV(ShlNV(v35, 7), v35))), InterleaveLOV(SubV(v30, SubV(ShlNV(v36, 7), v36)), SubV(v28, SubV(ShlNV(v35, 7), v35)))), InterleaveLOV(InterleaveHIV(SubV(v30, SubV(ShlNV(v36, 7), v36)), SubV(v28, SubV(ShlNV(v35, 7), v35))), InterleaveLOV(SubV(v30, SubV(ShlNV(v36, 7), v36)), SubV(v28, SubV(ShlNV(v35, 7), v35))))) & ShrNV(340282366920938463463374607431768211455, 8));
        v15 = v18;
    } while (&v1 != v14);
    _ZSt4cout.char_traits<char>>(&v0, strlen(&v0), v40);
    v41 = *((long long *)(240 + (char *)&_ZSt4cout + _ZSt4cout[24]));
    if (!v41)
        v42.__throw_bad_cast(); /* do not return */
    if (v41->field_38)
    {
        v43 = v41[1].padding_8[2];
    }
    else
    {
        v41._M_widen_init();
        v43 = 10;
        if (v41->field_0->field_30 != std::ctype<char>::do_widen)
            v43 = v41->field_0->field_30(v41);
    }
    (unsigned long long)_ZSt4cout.put(v43).flush();
    return;
}

void std::ctype<char>::do_widen(void* this, char arg_0)
{
    return;
}

void sub_401c24()
{
    return;
}


