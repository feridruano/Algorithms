# Generate Random Integers
from random import randint


# Combine Clothes and Sizes - 2 + 5N = O(N) - If 'sizes' was a random value, then it would be O(N^2)
def inventory(clothes, sizes):
    inventory = [] # 1 Step

    for clothing in clothes: # 5N Steps
        for size in range(1, sizes + 1): # M Steps - Always Constant - 5 Steps for each clothing
            inventory.append(clothing + " Size: " + str(size)) # ~1 Step

    return inventory # 1 Step


# Main Program
clothes = ["Purple Shirt", "Green Shirt", "Black Pants"]
sizes = 5 # Consider a Constant value instead of a random value - randint(1, 10) 

print("Clothes Available: %s" % clothes)
print("Sizes Available: %s" % sizes)
print("Clothes & Sizes Combinations: %s" % inventory(clothes, sizes))
