# Generate Random Numbers
from random import randint


# Staircase Algorithm for One, Two, or Three Steps at a Time.
def paths(steps):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    return paths(steps - 1) + paths(steps - 2) + paths(steps - 3)


# Main Program
staircase = []

for index in range(0, 3):
    staircase.append(randint(1,10))

print("Array of Different Staircases Steps: %s" % staircase)

for value in staircase:
    print("Number of Paths for %s-Step Staircase is: %s" % (value, paths(value)))
print()