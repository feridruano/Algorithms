# Generate Random Integers
from random import randint


# Average of All Even Numbers - 3N + 3 = O(N)
def average_of_evens(array):
    sum = 0.0 # 1 Step
    count = 0 # 1 Step

    for value in array: # 3N Steps - Worst-case all numbers are even
        if value % 2 == 0: # 1 Step
            sum += value # 1 Step
            count += 1 # 1 Step
    
    return sum / count # 1 Step


# Main Program    
array = []
for index in range(1, randint(0, 7)):
    array.append(randint(0, 32))

print("Array of Integers: %s" % array)
print("Average of Even Numbers: %s\n" % average_of_evens(array))
