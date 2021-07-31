# Palindrome Checker - Without Stack - 3 + ~6N / 2 = O(N)
def palindrome_checker(string):
    left_position = 0 # 1 Step
    right_position = len(string) - 1 # 1 Step

    while (left_position < right_position): # ~6N / 2 Steps
        if string[left_position].lower() != string[right_position].lower(): # 4 Step ? - Realization why we just consider these contants (i.e 1 comparison when complexity of comparison is low)
            return False # 1 Step
        left_position += 1 # 1 Step
        right_position -= 1 # 1 Step

    return True # 1 Step


# Main Program
strings = ["Racecar", "Kayak", "Deified", "Hannah", "AA", "AAA"]

for string in strings:
    print("Is %s a palindrome: %s" % (string, palindrome_checker(string)))
