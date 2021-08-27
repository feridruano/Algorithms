# Generate Random Integers
from random import randint


# Bubble Sort
def bubble_sort(array):
    for index in range(len(array) - 1): # N - 1 : (Size - (1) Zero-Based Array) - (1) Second to Last Element Using Exclusive Upper Limit From Range(Inclusive, Exclusive)
        for unsorted_index in range(len(array) - 1 - index): # N - i: (Size - (1) Zero-Based Array) - (i) Sorted Elements - (1) Last Unsorted Element Using Exclusive Upper Limit From Range(Inclusive, Exclusive)
            if array[unsorted_index] > array[unsorted_index + 1]:
                array[unsorted_index], array[unsorted_index + 1] = array[unsorted_index + 1], array[unsorted_index]
    return array


# Reversed Bubble Sort
def reversed_bubble_sort(array):
    for i in reversed(range(len(array) - 1)):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# Semi-Optimal Bubble Sort
def semi_optimal_bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for position in range(0, len(array) - 1):
            if array[position] > array[position + 1]:
                array[position], array[position + 1] = array[position + 1], array[position]
                sorted = False
    return array


# Main Program
array = []
for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))

print("Unsorted Array: %s" % array)
print("Bubble Sort: %s\n" % bubble_sort(array))

for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))
    
print("Unsorted Array: %s" % array)
print("Reverse Bubble Sort: %s\n" % reversed_bubble_sort(array))

for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))
    
print("Unsorted Array: %s" % array)
print("Semi-Optimial Bubble Sort: %s" % semi_optimal_bubble_sort(array))