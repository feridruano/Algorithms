# Generate Random Integers
from random import randint


# Two Number Products - 2 + N (N - 1) / 2 = O(N)
def two_number_products(array):
    products = [] # 1 Step

    for index in range(0, len(array) - 1): # N - 1 - Part of Inner Loop Big Oh Below
        for position in range(index + 1, len(array)): # N (N - 1) / 2 - Overall, Number of Steps
            print("Product: %s * %s" % (array[index], array[position]))
            products.append(array[index] * array[position]) # 2 Steps

    return products # 1 Step


# Main Program
array = list(range(1, randint(2, 6)))
print("Array of Numbers: %s" % (array))
print("Array of Two Number Products: %s\n" % two_number_products(array))
