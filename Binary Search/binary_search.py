# Generate Random Integers
from random import randint


# Iterative Binary Search
def iterative_binary_search(target, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Prevent Integer Overflow
        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# Recursive Binary Search
def recursive_binary_search(target, array, low, high):
    # Base Case
    if low > high:
        return False

    # Recursive Subproblem
    mid = low + (high - low) // 2  # Prevent Integer Overflow
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return recursive_binary_search(target, array, mid + 1, high)
    else:
        return recursive_binary_search(target, array, low, mid - 1)


# Main Program
array = list(range(1, randint(2, 32)))

# Search for Multiple Targets
for target in range(0, 3):
    target = randint(0, 32)
    print("Array: %s\nTarget: %s" % (array, target))
    print("Iterative Binary Search Found: %s" %
          iterative_binary_search(target, array))
    print("Recursive Binary Search Found: %s\n" %
          recursive_binary_search(target, array, 0,
                                  len(array) - 1))