from cs50 import *
from math import *

def main():
    text = get_string("Text: ")

    index = calculateRead(text)

    if(index < 1):
        print("Before Grade 1")
    elif(index > 16):
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def calculateRead(words):

    numberOfWords = 1.0
    numberOfletters = 0.0
    numberOfSentences = 0.0
    percentSentences = 0.0
    lastletterNotSpace = True

    i = 0
    n = len(words)
    while i < n:
        if(words[i]== " " and lastletterNotSpace):
            numberOfWords+=1.0
            lastletterNotSpace = False;

        elif(words[i]=="." or words[i]=="?" or words[i]=="!"):
            numberOfSentences+=1.0
            lastletterNotSpace = True

        elif(words[i].isalpha()):
            numberOfletters+=1.0
            lastletterNotSpace = True

        i+=1

    percentletter = numberOfletters/numberOfWords*100

    percentSentences = numberOfSentences/numberOfWords*100

    index  = round(0.0588 * percentletter - 0.296 * percentSentences - 15.8)

    return index

main()