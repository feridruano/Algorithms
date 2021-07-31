# Generate Random Integers
from random import randint


# Average Celsius and Fahrenheit Temperature - 8 + 2N + N Steps = O(N)
def average_temperature(fahrenheit_readings):
    average_temperatures = {} # 1 Step
    celsius_readings = [] # 1 Step

    for temperature in fahrenheit_readings: # 2N Steps
        celsius = (temperature - 32) * 5 / 9 # 1 Step
        celsius_readings.append(celsius) # 1 Step

    average_celsuis = 0.0 # 1 Step
    for temperature in celsius_readings: # N Steps
        average_celsuis += temperature # 1 Step

    average_temperatures['celsius'] = average_celsuis / len(celsius_readings) # 2 Steps
    average_temperatures['fahrenheit'] = (average_celsuis / len(celsius_readings) * 9 / 5) + 32 # 2 Steps ?

    return average_temperatures # 1 Step


# Main Program
fahrenheit_readings = []
for index in range(1, randint(2, 7)):
    fahrenheit_readings.append(randint(70, 95))

print("Fahrenheit Readings: %s" % fahrenheit_readings)
average_temperatures = average_temperature(fahrenheit_readings)
print("Average Celsius: %s" % average_temperatures['celsius'])
print("Average Fahrenheit: %s\n" % average_temperatures['fahrenheit'])