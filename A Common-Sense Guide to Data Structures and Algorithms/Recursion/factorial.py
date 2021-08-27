# Generate Random Integers
from random import randint


# Factorial
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


# Main Program
number = randint(0, 15)
print("Factorial of %s is: %s" % (number, factorial(number)))