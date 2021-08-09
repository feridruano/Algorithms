# Generate Random Numbers
from random import randint

# Need More Practice on 2D Arrays
# Shortest Grid Path From Top-Left Corner to Bottom-Right Corner
def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


def unique_paths(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1
    if not memo.get([rows, columns]):
        memo[[rows, columns]] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
    return memo[[rows, columns]]


# Main Program
rows = randint(1, 5)
columns = randint(1, 5)
print("The Shortest Grid Path for a %sx%s Grid is: %s\n" % (rows, columns, unique_paths(rows, columns)))