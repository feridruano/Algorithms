# Generate Random Integers
from random import randint


# Count the Ones - Tricky, it's 2 + 2N Steps = O(N). Out of all of the ragged arrays, we simple check each value once.
#   Therefore, we make N passes/checks/whatevers as the outer loop just iterates over the ragged arrays.
#   Imagine putting all the ragged array 0s and 1s into one really long array of 0s and 1s. That's 2N Steps to loop through.
def count_ones(two_dimensional_array):
    count_of_ones = 0 # 1 Step

    for array in two_dimensional_array: # N Steps for Number of Ragged Arrays - Ignored
        for value in array: # 2M Steps per Ragged Array
            if value == 1: # 1 Step
                count_of_ones += 1 # 1 Step

    return count_of_ones # 1 Step


# Main Program
array_of_arrays = []

# Generate Two Dimensional Ragged Array of 0s and 1s
for one_dimesional_index in range(0, randint(2, 10)):
    array_of_arrays.append([])
    for two_dimesional_index in range(0, randint(2, 10)):
        (array_of_arrays[one_dimesional_index]).append(randint(0,1))

print("Clothes Available: %s" % array_of_arrays)
print("Number of 1s: %s" % count_ones(array_of_arrays))