# Array Intersection
def intersection(array_1, array_2):
    intersection = []
    hash_table = {}

    for value in array_1:
        hash_table[value] = True

    for value in array_2:
        if hash_table.get(value):
            intersection.append(value)

    return intersection


# Main Program
array_1 = ["a", "b", "c", "d", "e", "f"]
array_2 = ["b", "d", "f"]
print("%s - Array 1" % array_1)
print("%s - Array 2" % array_2)
print("%s - Intersection" % (intersection(array_1, array_2)))