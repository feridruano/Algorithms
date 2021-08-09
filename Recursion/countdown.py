# Generate Random Integers
from random import randint


# Recursive Countdown
def countdown(time):
    if time == 0: 
        print("Liftoff")
    else:
        print("%s" % time)
        countdown(time - 1)


# Main Program
time = randint(10, 20)
countdown(time)
