# Recursive 'nth' Fibonaci Sequence Algorithm
def fibonaci(nth):
    if nth < 2:
        return nth
    return fibonaci(nth - 2) + fibonaci(nth - 1)

# Main Program
for number in range(0, 10):
    print("The Fibonaci Sequence of %s is: %s" % (number, fibonaci(number)))