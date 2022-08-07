#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Prompt user to agree wiht something
    char c = get_char("Do you agree? ");

    //cehck wether user agrees
    if(c == 'y' || c=='Y')
    {
        printf("Agreed.\n");
    }
    if (c=='n' || c =='N')
    {
        printf("Not agreed.\n");
    }
}