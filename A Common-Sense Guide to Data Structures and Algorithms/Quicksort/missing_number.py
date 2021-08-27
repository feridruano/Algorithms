# The following function finds the “missing number” from an array of integers. 
# That is, the array is expected to have all integers from 0 up to the
# array’s length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is
# missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the
# number 8.
# Use sorting to write a new implementation of this function that only takes
# O(N log N). (There are even faster implementations, but we’re focusing on
# using sorting as a technique to make code faster.)

# Generate Random Numbers
from random import randint


# Partition Array for Pivot Index
def partition(array, start, end):
    pivot = array[end]
    left_pointer = start
    right_pointer = end - 1

    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1
        while array[right_pointer] > pivot:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        else:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            left_pointer += 1
    array[left_pointer], array[end] = array[end], array[left_pointer]
    return left_pointer


# Quicksort - O(N Log N)
def quicksort(array, start, end):
    if end - start <= 0:
        return
    pivot_index = partition(array, start, end)
    quicksort(array, start, pivot_index - 1)
    quicksort(array, pivot_index + 1, end)
    return array


array = []
for index in range(0, randint(3, 5)):
    array.append(randint(1,10))
print("Array: %s" % array)
quicksort(array, 0, len(array) - 1)
missing_number = -1
for index in range(0, len(array)):
    if array[index] != index:
        missing_number = index
        break
print("Missing Numbers: %s" % missing_number)