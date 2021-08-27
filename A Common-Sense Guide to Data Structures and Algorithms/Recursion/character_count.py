# Generate Random Numbers
from random import randint


# Character Count - All Strings
def character_count(array):
    if len(array) == 0:
        return 0
    return len(array[0]) + character_count(array[1 : len(array)])


# Main Program
array = []

for iter in range(1, randint(2, 5)):
    string = ''
    for position in range(1, randint(2, 10)):
        string += chr(randint(97, 122))
    array.append(string)

print("The Array of Strings is: %s" % array)
print("The Total Character is: %s\n" % character_count(array))