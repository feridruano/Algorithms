# Generate Random Integers
from random import randint


# Bubble Sort
def bubble_sort(collection):
    for i in range(len(collection) - 1): # N - 1 : (Size - (1) Zero-Based Array) - (1) Second to Last Element Using Exclusive Upper Limit From Range(Inclusive, Exclusive)
        for j in range(len(collection) - 1 - i): # N - i: (Size - (1) Zero-Based Array) - (i) Sorted Elements - (1) Last Unsorted Element Using Exclusive Upper Limit From Range(Inclusive, Exclusive)
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

# Reversed Bubble Sort
def reversed_bubble_sort(collection):
    for i in reversed(range(len(collection) - 1)):
        for j in range(0, i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

# Main Program
collection = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(collection)
print("%s - Bubble Sort" % (collection))
collection = [72, 5, 32, 12, 26, 11, 90]
reversed_bubble_sort(collection)
print("%s - Reversed Bubble Sort" % (collection))