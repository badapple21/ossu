#include <cs50.h>
#include <stdio.h>

int main(void)
{
    const int MINE = 2;
    int points = get_int("How many points did you lose? ");

    if(points < MINE)
    {
        printf("You lost fewer points then me.\n");
    }
    else if (points > MINE)
    {
        printf("you lost more points then me.\n");
    }
    else
    {
        printf("You lost the same number of points as me.\n");
    }
}