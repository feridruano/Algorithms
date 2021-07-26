# Generate Random Integers
from random import randint


# Insertion Sort - Sorted On The Left Side Of the Array
def insertion_sort(array):
    for index in range(1, len(array)):
        for position in reversed(range(1, index + 1)):
            if(array[position - 1] > array[position]):
              array[position], array[position - 1] = array[position - 1], array[position]
            else:
                continue
    return array


# Insertion Sort - Sorted On the Right Side Of the Array
def reversed_insertion_sort(array):
    for index in reversed(range(0, len(array) - 1)):
        for position in range(index, len(array) - 1):
            if array[position + 1] < array[position]:
                array[position], array[position + 1] = array[position + 1], array[position]
            else:
                continue
    return array


# Main Program
array = []
for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))

print("Unsorted Array: %s" % array)
print("Selection Sort: %s\n" % insertion_sort(array))

for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))

print("Unsorted Array: %s" % array)
print("Reversed Selection Sort: %s\n" % reversed_insertion_sort(array))