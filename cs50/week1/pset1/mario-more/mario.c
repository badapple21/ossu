#include <cs50.h>
#include <stdio.h>

int main(void)
{
// gets height from user
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while(n < 1);

    
    // main loop
    for(int i = 0; i<n;i++){

        // print white spaces
        for(int j = n-(i+1); j > 0;j--)
        {
            printf(" ");
        }

        //prints first column of #
        for(int l = n-(i+1); l < n;l++)
        {
            printf("#");
        }

        // prints gap
        printf("  ");

        // prints 2nd column
        for(int t = n-(i+1); t<n;t++)
        {
            printf("#");
        }

        //newline
        printf("\n");
    }
}