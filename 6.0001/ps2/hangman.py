# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from traceback import print_tb
from wsgiref import validate
from zoneinfo import available_timezones

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # sets up variable secret_word_letters
    secret_word_letters = []

    # loops through the letters in secret_word and adds them to secret_word_letters
    for letter in secret_word:
        secret_word_letters.append(letter)

    # checks if the list are the same
    return secret_word_letters == secret_word


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # sets up rtn
    rtn = ""

    # loops through the letters in secret_word and checks if they are in letters_guessed
    for letter in secret_word:
        if letter in letters_guessed:
            rtn = rtn + letter
        else:
            rtn = rtn + " _ "

    return rtn


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # sets up rtn string and available_letters
    rtn = ""
    available_letters = string.ascii_lowercase

    # loops through available_letters and checks if they have been guessed so far
    for letter in available_letters:
        if letter not in letters_guessed:
            rtn += letter

    return rtn


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # sets up secret_word the length of the secret_word guesses game over warnings  guess_good
    secret_word = secret_word
    secret_word_length = len(secret_word)
    guesses = 6
    warnings = 3
    game_over = False
    guessed_letters = []
    vowels = "aeiou"

    # introduces user to the game
    print("Welcome to the game Hangman!")
    print(
        f"I am thinking of a word that is {secret_word_length} letters long.")

    # main game loop
    while not game_over:

        available_letters = get_available_letters(guessed_letters)

        # rests guess_good variable
        guess_good = True

        # tells the user how many guesses they have left and available_letters
        print("-----------------------------------------------")
        # resets available letters
        if(is_word_guessed(secret_word, guessed_letters)):
            print("congratulations, you won!")
            return

        elif(guesses <= 0):
            print("Oops Out of guesses")
            print(
                f"The word was {secret_word}. Better luck next time ¯\_(ツ)_/¯ ")
            return
        print(f"you have {warnings} warnings left.")
        print(f"you have {guesses} guesses left.")
        print(f"available letters: {available_letters}")
        print(f"{get_guessed_word(secret_word, guessed_letters)}")

        # prompts the user for a guess
        guess = input("Enter a guess: ").lower()

        # validates guess
        if guess not in string.ascii_lowercase:
            guess_good = False
            print("Oops! Thats not a letter")
            warnings -= 1
            if(warnings == -1):
                guesses -= 1
                warnings = 3

            print(
                "Oops! Thats not a valid letter. You now have {warnings} warnings:")
            print(f"{get_guessed_word(secret_word, guessed_letters)}")

        elif guess not in get_available_letters(guessed_letters):
            guess_good = False
            warnings -= 1
            if(warnings == -1):
                guesses -= 1
                warnings = 3

            print(
                f"Oops! You've already guessed that letter. You now have {warnings} warnings:")
            print(f"{get_guessed_word(secret_word, guessed_letters)}")

        # adds the guess to letters_guessed
        if guess_good:
            guessed_letters.append(guess)
            available_letters = get_available_letters(guessed_letters)
            if guess in secret_word:
                print(
                    f"Good guess: {get_guessed_word(secret_word, guessed_letters)}")

            else:
                print("Oops! Thats not a letter in my word.")
                if(guess in vowels):
                    guesses -= 2
                else:
                    guesses -= 1


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word, letters):

    # removes white space from word
    my_word = my_word.replace(" ", "")


    # checks if the words are the same length
    if(len(my_word) != len(other_word)):
        return False

    # loops through each index of my word and i it gets to a letter in my_word it checks if the other words has the same letter at that same index
    for i in range(len(my_word)-1):
        if(my_word[i] != "_"):
            if(other_word[i] != my_word[i]):
                return False
        else:

          #checks if the letter in other word at that index has already been guessed
          if(other_word[i] in letters):
            return False

    # if the interpeter has gotten this far then both words have the same letters at the same indexes
    return True


def show_possible_matches(my_word, letters):
    # sets up variable that will conation all words that math at the end
    possible_matches = []

    # loops through all the words in words list and runs them trough the match_with_gaps function and if they match adds them to possible matches
    for word in wordlist:
        if match_with_gaps(my_word, word, letters):
            possible_matches.append(word)

    # check is possible matches is empty
    if(possible_matches == []):
        print("No matches found")
    else:

        # prints out matches
        # sets rtn string
        rtn = ""
        for match in possible_matches:
            rtn = rtn + match + " "

        print(rtn)


def hangman_with_hints(secret_word):
    # sets up secret_word the length of the secret_word guesses game over warnings  guess_good
    secret_word = "blowhard"
    secret_word_length = len(secret_word)
    guesses = 6
    warnings = 3
    game_over = False
    guessed_letters = []
    vowels = "aeiou"

    # introduces user to the game
    print("Welcome to the game Hangman!")
    print(
        f"I am thinking of a word that is {secret_word_length} letters long.")

    # main game loop
    while not game_over:

        available_letters = get_available_letters(guessed_letters)

        # rests guess_good variable
        guess_good = True

        # tells the user how many guesses they have left and available_letters
        print("-----------------------------------------------")
        # resets available letters
        if(is_word_guessed(secret_word, guessed_letters)):
            print("congratulations, you won!")
            return

        elif(guesses <= 0):
            print("Oops Out of guesses")
            print(
                f"The word was {secret_word}. Better luck next time ¯\_(ツ)_/¯ ")
            return
        print(f"you have {warnings} warnings left.")
        print(f"you have {guesses} guesses left.")
        print(f"available letters: {available_letters}")
        print(f"{get_guessed_word(secret_word, guessed_letters)}")

        # prompts the user for a guess
        guess = input("Enter a guess: ").lower().strip()

        # check if the guess is *
        if(guess == "*"):

            # prints possible words
            show_possible_matches(get_guessed_word(
                secret_word, guessed_letters), guessed_letters)

        else:

            # validates guess
            if guess not in string.ascii_lowercase:
                guess_good = False
                print("Oops! Thats not a letter")
                warnings -= 1
                if(warnings == -1):
                    guesses -= 1
                    warnings = 3

                print(
                    "Oops! Thats not a valid letter. You now have {warnings} warnings:")
                print(f"{get_guessed_word(secret_word, guessed_letters)}")

            elif guess not in get_available_letters(guessed_letters):
                guess_good = False
                warnings -= 1
                if(warnings == -1):
                    guesses -= 1
                    warnings = 3

                print(
                    f"Oops! You've already guessed that letter. You now have {warnings} warnings:")
                print(f"{get_guessed_word(secret_word, guessed_letters)}")

            # adds the guess to letters_guessed
            if guess_good:
                guessed_letters.append(guess)
                available_letters = get_available_letters(guessed_letters)
                if guess in secret_word:
                    print(
                        f"Good guess: {get_guessed_word(secret_word, guessed_letters)}")

                else:
                    print("Oops! Thats not a letter in my word.")
                    if(guess in vowels):
                        guesses -= 2
                    else:
                        guesses -= 1


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
