# First Non-Duplicated Character
def non_duplicated_character(string):
    hash_table = {}
    string = string.lower()

    for character in string:
        if hash_table.get(character):
            hash_table[character] += 1
        else:
            hash_table[character] = 1

    for character in string:
        if hash_table.get(character) == 1:
            return character

    return None


# Main Program
print("%s - First Non-Duplicated Character" %
      non_duplicated_character("Minimum"))
      