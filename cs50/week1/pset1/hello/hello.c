#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // ask user for name
    string name = get_string("Whats your name? ");

    //prints out hello + name
    printf("hello, %s\n", name);
}