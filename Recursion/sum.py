# Generate Random Integers
from random import randint


# Sum of Array Numbers
def sum(array):
    if len(array) == 1: 
        return array[0]
    else:
        return array[0] + sum(array[1 : len(array)]) # 1 + CALL([2,3]) = 1 + 5 = 6


# Main Program
array = []

for iter in range(1, randint(1, 10)):
    array.append(randint(0, 32))

print("Array of Numbers: %s" % array)
print("Sum of Array Numbers is: %s\n" % sum(array))    