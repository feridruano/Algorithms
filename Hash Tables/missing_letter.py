# Missing Letter From Alphabet - Task is to return the ONE missing letter only. Adjust input accordingly.
def missing_string(string):
    alphabet = list(map(chr, range(97, 123)))
    hash_table = {}

    for character in string:
        hash_table[character] = True

    for letter in alphabet:
        if not hash_table.get(letter):
            return letter
    
    return None

# Main Program
print("%s - Missing Letter" % missing_string("the quick brown box jumps over a lazy dog"))