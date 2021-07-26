# Generate Random Integers
from random import randint


# Selection Sort - Smallest Values Sorted First
def selection_sort(array):
    for index in range(0, len(array) - 1):
        lowest_value_index = index
        for position in range(index + 1, len(array)):
            if(array[lowest_value_index] > array[position]):
                lowest_value_index = position
        array[index], array[lowest_value_index] = array[lowest_value_index], array[index]
    return array

# Reversed Selection Sort - Largest Values Sorted First
def reversed_selection_sort(array):
    for index in reversed(range(1, len(array))):
        highest_value_index = index
        for position in reversed(range(0, index - 1)):
            if(array[highest_value_index] < array[position]):
                highest_value_index = position
        array[index], array[highest_value_index] = array[highest_value_index], array[index]
    return array


# Main Program
array = []
for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))

print("Unsorted Array: %s" % array)
print("Selection Sort: %s\n" % selection_sort(array))

for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))

print("Unsorted Array: %s" % array)
print("Reversed Selection Sort: %s\n" % reversed_selection_sort(array))