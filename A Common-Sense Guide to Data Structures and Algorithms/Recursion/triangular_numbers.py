# Generate Random Numbers
from random import randint

# Triangular Number at Nth Position
def triangular_number(position):
    if position == 1:
        return 1
    return position + triangular_number(position - 1)


# Main Program
array = []

for iter in range(1, randint(1, 10)):
    array.append(randint(0, 32))

print("Array of Numbers: %s" % array)
for value in array:
    print("Triangular Number of Position %s is: %s" % (value, triangular_number(value)))  
print()