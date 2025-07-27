int main()
{
    int i = 0;
    char *str = "€";

    while (str[i])
    {
        i++;
    }
    printf("i == %d\n", i)
}