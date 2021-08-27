# Reverse String
def reverse_string(string):
    stack = []

    for character in string:
        stack.append(character)

    string = ""
    while stack:
        string += stack.pop()

    return string


# Main Program
array = ["Potato", "Tomato", "Racecar", "Train"]
for value in array:
    print("String: %s | Reversed: %s" % (value, reverse_string(value)))