# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    possiblities = []

    if(len(sequence)==1):
        return [sequence]
    else:
        length = len(sequence)
        letter = sequence[0]
        sequence = sequence[1:]
        for possiblity in get_permutations(sequence):
            for i in range(length):
                possiblities.append(insert_letter(i, possiblity, letter))
    return possiblities

def insert_letter(place, string, letter):
    if(place==0): 
        return f"{letter}{string}"
    else:
        return f"{string[:place]}{letter}{string[place:]}"


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
#unit test for insert_letter
#   print(insert_letter(0, "ust", "b"))\
#   print(insert_letter(1, "ust", "b"))
#   print(insert_letter(2, "ust", "b"))

    print(get_permutations("abc"))
    print(get_permutations("bust"))
    print(get_permutations("ab"))
