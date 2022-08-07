#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // gets number from user
    long number;
    number = get_long("Number: ");

    //sets up varibles
    float x = 1;
    int n = -1;
    float y = 1;
    int odd = -1;
    int sum = 0;
    long z = 10;
    int firstDigit = 0;
    string manufactor = "INVALID";

    //gets legnth of number
    //calculates numebr of digits
    while(y>=1)
    {
        y = number/x;
        x*=10;
        n+=1;
    }

    if(n==13 || n==16 || n==15){

    for(int i = n; i > 0;i--)
    {
        int digit = number % z;
        if(i==2){
            firstDigit+=digit;
        }if(i==1){
            firstDigit+=digit*10;
        }

        if(odd==-1){
            sum+=digit;
        }else if(odd==1){
            if(digit*2>=10){
                digit*=2;
                int digit2 = digit % 10;
                sum+=digit2 + (digit/10);

            }else{
                sum+=digit*=2;
            }

        }
        odd = odd * -1;
        number /= 10;
        }

    if(firstDigit==34 || firstDigit == 37){
         manufactor = "AMEX";
    }
    if(firstDigit==51 || firstDigit == 52 || firstDigit == 53 || firstDigit == 54 || firstDigit == 55){
         manufactor = "MASTERCARD";
    }
    if(firstDigit/10==4){
         manufactor = "VISA";
    }
    if(sum%10==0){
        printf("%s\n", manufactor);
    }else{
        printf("INVALID\n");
    }
    }
    else{
        printf("INVALID\n");
    }

}