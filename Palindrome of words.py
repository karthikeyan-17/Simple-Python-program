''' A palindrome is a word that is spelled the same backward and
forward, like “noon”and “redivider”.Recursively, a word is a palindrome
if the first and last letters are thesame and the middle is a palindrome.
The following are functions that take a stringargument and return the
first, last, and middle letters:

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
        return word[1:-1]

1.Type these functions into a file named palindrome.py and test them out.
Whathappens if you call middle with a string with two letters? One letter?
Whatabout the empty string, which is written “” and contains no letters?

2.Write a function called is_palindrome that takes a string argument and
returnsTrue if it is a palindrome and False otherwise. Remember that you
can usethe built-in function len to check the length of a string. '''


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if first(word) == last(word):
        if len(word) <= 2:
            print('True')
        else:
            is_palindrome(middle(word))
            print(word[1:-1])
    else:
        print('False')

word = input('Enter the word to check:')
       
is_palindrome(word)


