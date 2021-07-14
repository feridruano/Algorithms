# Generate Random Integers
from random import randint


# Linear Search
def linear_search(value, collection):
    for item in collection:
        if item == value:
            return True
    return False


# Main Program
collection = list(range(1, randint(0, 32)))
value = randint(0, 32)
result = linear_search(value, collection)
print("%s, %s is in %s - Linear Search" % (result, value, collection))
