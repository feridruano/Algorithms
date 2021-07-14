# Generate Random Integers
from random import randint


# Insertion Sort - Sorted On The Left Side Of the Array
def insertion_sort(collection):
    for index in range(1, len(collection)):
        for position in reversed(range(1, index + 1)):
            if(collection[position - 1] > collection[position]):
              collection[position], collection[position - 1] = collection[position - 1], collection[position]
            else:
                continue


# Insertion Sort - Sorted On the Right Side Of the Array
def right_insertion_sort(collection):
    for index in reversed(range(0, len(collection) - 1)):
        for position in range(index, len(collection) - 1):
            if collection[position + 1] < collection[position]:
                collection[position], collection[position + 1] = collection[position + 1], collection[position]
            else:
                continue


# Main Program
collection = [93, 34, 25, 12, 22, 11, 90, 5]
insertion_sort(collection)
print("%s - Insertion Sort" % (collection))
collection = [84, 45, 32, 12, 26, 11, 72, 5]
right_insertion_sort(collection)
print("%s - Reversed Selection Sort" % (collection))