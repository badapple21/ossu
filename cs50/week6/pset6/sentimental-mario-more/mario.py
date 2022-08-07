# TODO
from cs50 import get_int


while True:
    n = get_int("Size: ")
    if (n > 0) and (n < 9):
        break

for i in range(n):

    j = n - (i+1)
    while j > 0:
        print(" ", end="")
        j-=1

    l = n - (i+1)

    while l < n:
        print("#", end="")
        l+=1

    print("  ", end="")

    t = n - (i+1)

    while t < n:
        print("#", end="")
        t+=1


    print("")
