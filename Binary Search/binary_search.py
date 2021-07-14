# Generate Random Integers
from random import randint


# Recursive Implementation
def recursive_binary_search(value, collection, low, high):
    if low > high:
        return False

    mid = low + (high - low) // 2
    if collection[mid] == value:
        return True
    elif collection[mid] < value:
        return recursive_binary_search(value, collection, mid + 1, high)
    else:
        return recursive_binary_search(value, collection, low, mid - 1)


# Iterative Implementation
def iterative_binary_search(value, collection):
    low = 0
    high = len(collection) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if collection[mid] == value:
            return True
        elif collection[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False        


# Main Program
collection = list(range(1, randint(0, 32)))
value = randint(0, 32)
recursive_result = recursive_binary_search(value, collection, 0,
                                           len(collection) - 1)
iterative_result = iterative_binary_search(value, collection)
print("%s, %s is in %s - Recursive Solution" %
      (recursive_result, value, collection))
print("%s, %s is in %s - Iterative Solution" %
      (iterative_result, value, collection))
