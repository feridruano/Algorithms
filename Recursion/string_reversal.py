# Generate Random Numbers
from random import randint


# String Reversal
def string_reversal(string):
    if len(string) == 1:
        return string[0]
    else:
        return string_reversal(string[1 : len(string)]) + string[0] # CALL("BC") + "A" = "CB" + "A" = "CBA"


# Main Program
string = ''
for position in range(1, randint(2, 10)):
    string += chr(randint(97, 122))
print("The String is: %s" % string)
print("The String Reversal is: %s\n" % string_reversal(string))
