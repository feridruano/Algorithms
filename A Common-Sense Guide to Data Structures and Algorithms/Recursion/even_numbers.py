# Generate Random Numbers
from random import randint


# Even Numebers Only Recursively
def evens(array):
    if len(array) == 0:
        return []

    if array[0] % 2 == 0:
        return [array[0]] + evens(array[1 : len(array)])
    else:
        return evens(array[1 : len(array)])

    
# Main Program
array = [2,1,4]

# for iter in range(1, randint(1, 10)):
#     array.append(randint(0, 32))

print("Array of Numbers: %s" % array)
print("Evens of Array are: %s\n" % evens(array))    