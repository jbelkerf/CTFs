#include <stdlib.h>
#include <stdio.h>

int main()
{
    FILE * f = fopen("flag.txt", "r");
    printf("%p   \n", f);
}