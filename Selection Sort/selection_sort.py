# Generate Random Integers
from random import randint


# Selection Sort - Smallest Values Sorted First
def selection_sort(collection):
    for index in range(0, len(collection) - 1):
        lowest_value_index = index
        for position in range(index + 1, len(collection)):
            if(collection[lowest_value_index] > collection[position]):
                lowest_value_index = position
        collection[index], collection[lowest_value_index] = collection[lowest_value_index], collection[index]


# Reversed Selection Sort - Largest Values Sorted First
def reversed_selection_sort(collection):
    for index in reversed(range(1, len(collection))):
        highest_value_index = index
        for position in reversed(range(0, index - 1)):
            if(collection[highest_value_index] < collection[position]):
                highest_value_index = position
        collection[index], collection[highest_value_index] = collection[highest_value_index], collection[index]


# Main Program
collection = [64, 34, 25, 12, 22, 11, 90]
selection_sort(collection)
print("%s - Selection Sort" % (collection))
collection = [72, 5, 32, 12, 26, 11, 83]
reversed_selection_sort(collection)
print("%s - Reversed Selection Sort" % (collection))