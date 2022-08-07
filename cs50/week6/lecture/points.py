from cs50 import get_int

points = get_int("How many points did you lose? ")

if points < 2:
    print("You lost fewer points then me.")
elif points > 2:
    print("You lost more points then me")
else:
    print("You lost the same number of points as me")