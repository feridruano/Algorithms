# Generate Random Numbers
from random import randint


# Index of First X Character - At least one instance of the character X exists
def index_of(string):
    if string[0] == "x":
        return 0
    
    return index_of(string[1 : len(string)]) + 1


# Main Program
string = "abcdefghijklmnopqrstuvwxyz"
print("The String is: %s" % string)
print("The Anagrams are: %s\n" % index_of(string))