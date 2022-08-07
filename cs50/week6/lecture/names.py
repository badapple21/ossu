import sys

names = ["Bill", "Charlie", "Fred", "George", "Percy", "Ron"]

if "Ron" in names:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)