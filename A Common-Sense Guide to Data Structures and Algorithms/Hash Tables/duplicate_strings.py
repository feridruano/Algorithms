# Duplicate Strings
def duplicate_strings(array):
    duplicate_strings = []
    hash_table = {}

    for value in array:
        if hash_table.get(value):
            duplicate_strings.append(value)
        else:
            hash_table[value] = True
            
    return duplicate_strings


# Main Program
array = ["a", "b", "c", "d", "c", "e", "f"]
print("%s - Array of Strings" % array)
print("%s - Duplicate Strings" % duplicate_strings(array))
