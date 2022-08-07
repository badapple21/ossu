from cs50 import get_int
from math import *

number = get_int("Number: ")

x = 1
n = -1
y = 1
odd = -1
sums = 0
z = 10
firstDigit = 0
manufactor = "INVALID"

while y >= 1:
    y = number/x
    x*=10
    n+=1

if ((n == 13) or (n == 16) or (n == 15)):
    i = n
    while i > 0:
        digit = floor(number % z)
        if(i==2):
            firstDigit+=digit
        if(i==1):
            firstDigit+=digit*10

        if(odd==-1):
            sums+=digit
        elif(odd==1):
            if(digit*2>=10):
                digit*=2
                digit2 = digit % 10
                sums+=digit2 + (digit/10);
            else:
                digit = digit * 2
                sums+=digit
        odd = odd * -1
        number /= 10
        sums = int(sums)
        i-=1
    if(firstDigit==34 or firstDigit == 37):
        manufactor = "AMEX"

    if(firstDigit==51 or firstDigit==52 or firstDigit == 53 or firstDigit == 54 or firstDigit == 55):
        manufactor = "MASTERCARD"

    vdigit = int(firstDigit/10)

    if(vdigit==4):
        manufactor = "VISA"

    if(round(sums%10==0)):
        print(manufactor)

    else:
        print("INVALID")
else:
    print("INVALID")