#include <stdio.h>
int main()
{
    int num, rev = 0, rem;
    printf("Enter a 3-digit num: ");
    scanf("%d", &num);
    if (num < 100 || num > 999)
    {
        printf("Error: Please enter a valid 3-digit number.\n");
        return 1;
    }
    printf("Original num: %d\n", num);
    while (num != 0)
    {
        rem = num % 10;
        rev = rev * 10 + rem;
        num = num / 10;
    }

    printf("rev num: %d\n", rev);

    return 0;
}