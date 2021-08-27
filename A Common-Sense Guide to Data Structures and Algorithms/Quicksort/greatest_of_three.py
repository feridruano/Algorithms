# Given an array of positive numbers, write a function that returns the
# greatest product of any three numbers. The approach of using three
# nested loops would clock in at O(N3), which is very slow. Use sorting to
# implement the function in a way that it computes at O(N log N) speed.
# (There are even faster implementations, but we’re focusing on using
# sorting as a technique to make code faster.)

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


# Quickselect Algorithm - O(N) - Average | O(N^2) - Worst
def quickselect(array, position, start, end):
    if end - start <= 0:
        return array[start]
    pivot_index = partition(array, start, end)
    if position < pivot_index:
        return quickselect(array, position, start, pivot_index - 1)
    elif position > pivot_index:
        return quickselect(array, position, pivot_index + 1, end)
    else:
        return array[pivot_index]


# Greatest Product of Three Values - O(N)
def greatest_of_three(array):
    numbers = []
    product = 1
    for position in range(len(array) - 3, len(array)):
        largest_at_position = quickselect(array, position, 0, len(array) - 1)
        numbers.append(largest_at_position)
        product = product * largest_at_position
    numbers.append(product)
    return numbers


# Quicksort - O(N Log N)
def quicksort(array, start, end):
    if end - start <= 0:
        return
    pivot_index = partition(array, start, end)
    quicksort(array, start, pivot_index - 1)
    quicksort(array, pivot_index + 1, end)
    return array


# Main Program
# array = [1, 1, 4, 1] # Debug
array = []
for index in range(0, randint(3, 5)):
    array.append(randint(1,10))
print("Array: %s" % array)
result = greatest_of_three(array)
print("Quickselect - O(N) - The Greatest Product of Three is: %s * %s * %s = %s" % (result[0], result[1], result[2], result[3]))

# array = [1, 1, 4, 1] # Debug
array = []
for index in range(0, randint(3, 5)):
    array.append(randint(1,10))
print("Array: %s" % array)
quicksort(array, 0, len(array) - 1)
array_length = len(array)
print("Quicksort - O(N Log N) - The Greatest Product of Three is: %s * %s * %s = %s" % (array[array_length - 3], array[array_length - 2], array[array_length - 1], array[array_length - 3] * array[array_length - 2] * array[array_length - 1]))