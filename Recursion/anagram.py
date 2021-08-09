# Generate Random Numbers
from random import randint


# Anagrams
def anagrams(string):
    if len(string) == 1:
        return [string[0]]
    
    collection = []
    
    substring_anagrams = anagrams(string[1 : len(string)]) # Returns a list of anagrams

    for anagram in substring_anagrams: # Create more anagrams from each anagram in the list of anagrams
        for position in range(0, len(string) + 1):
            copy = anagram[:]
            copy = copy[:position] + string[0] + copy[position:] 
            collection.append(copy)

    return collection


# Main Program
string = ''
for position in range(1, randint(2, 5)):
    string += chr(randint(97, 122))
print("The String is: %s" % string)
print("The Anagrams are: %s\n" % anagrams(string))