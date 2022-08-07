import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage Wrong")

    database = []
    STR = []
    # TODO: Read database file into a variable
    with open(sys.argv[1], newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        for person in reader:
            database.append(person)

    with open(sys.argv[1], newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            STR.append(row)
            break
    STR = STR[0]
    STR.remove("name")



    # TODO: Read DNA sequence file into a variable
    sequence = ""
    with open(sys.argv[2]) as file:
        reader = csv.reader(file)
        for line in reader:
            sequence = line[0]

    # create a dict keeping track of all the sequnce matches
    matches = {}
    for sample in STR:
        matches[sample] = 0





    # TODO: Find longest match of each STR in DNA sequence
    for sample in STR:
        matches[sample] = longest_match(sequence, sample)

    # TODO: Check database for matching profiles

    for person in database:
        posible_match = True
        i = 0
        while posible_match and i < len(STR):
            if(int(person.get(STR[i]))==int(matches.get(STR[i]))):
                posible_match = True
            else:
                posible_match = False
            i+=1
        if posible_match:
            print(person.get("name"))
            sys.exit(0)

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    #print(longest_run)
    return longest_run


main()
