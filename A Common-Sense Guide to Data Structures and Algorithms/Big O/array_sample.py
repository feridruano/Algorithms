# Generate Random Integers
from random import randint


# Array Sample - First, Middle, Last - ~ 5 Steps = O(1)
#   O(1) - A Constant number of operations for each array, regardless of array size.
def array_sample(array):
    first = array[0] # 1 Step
    middle = array[len(array) // 2] # ~ 3 Steps
    last = array[-1] # 1 Step

    return [first, middle, last]


# Main Program    
array = []
for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))

print("Array of Integers: %s" % array)
print("Array Sample: %s\n" % array_sample(array))