#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Input:  ");
    printf("OUTPUT: ");
    for(int i = 0, int n = strlen(s); i < n; i++)
    {
        printf("%C", s[i]);
    }
    printf("\n");
}