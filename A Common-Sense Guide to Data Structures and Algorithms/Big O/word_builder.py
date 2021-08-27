# Word Builder - Every Two Charater Combination of Characters. - 3N * 3N + 2 = O(N^2)
#   Palindorme chacters are allowed, but not of the same characters.
def word_builder(characters):
    combinations = [] # 1 Step

    for character in characters: # 3N Steps ? - I Not Sure of the Constant Number of Steps For Outer Loop. I understand why it's N^2.
        for position_value in characters: # 3N Steps
            if character != position_value: # 1 Step
                combinations.append(character + position_value) # 2 Steps

    return combinations # 1 Step


# Main Program
characters = ["a", "b", "c", "d"]
print("Array of Characters: %s" % characters)
print("Two Character Combinations: %s\n" % word_builder(characters))