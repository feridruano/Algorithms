# Generate Random Integers
from random import randint


# Linear Search
def linear_search(target, array):
    for value in array:
        if value == target:
            return True
    return False


# Main Program
array = list(range(1, randint(0, 32)))

# Search for Multiple TargetsP
for target in range(0, 3):
    target = randint(0, 32)
    print("Array: %s\nTarget: %s" % (array, target))
    print("Linear Search Target Found: %s\n" % linear_search(target, array))