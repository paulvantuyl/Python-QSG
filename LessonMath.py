import math
from decimal import Decimal
import statistics

# Ask the user for a numb4er
number = input("Please enter a number: ")

# Convert to an int
number = int(number)

test = 4

# Calculate the result
result = math.sqrt(number)

# Display the result
# I think that format(number, result) is what's putting values into {:n} and {:.6f}
print("The square root of {:n} is {:.6f}".format(number, result))

print("\n")

# Convert integer to floating-point
int_number = 5
floating_number = float(int_number)

# Display both
print(int_number)
print(floating_number)

print("\n")

a = 1.2
b = 1.49
c = 1.51

# Displaying results
print(round(a))
print(round(b))
print(round(c))

print("\n")

n = 0.2 + 0.2 + 0.2
print("The total is {:.2f}".format(n))

# Display n with 30 decimal precision
print("The toal is actually {:.30f}".format(n))

# In order to deal with precision in floating points we need to import
# the Decimal class from the decimal module
# from decimal import Decimal

print("Use Decimal to math it correctly ----->")

d = Decimal("0.2")
e = Decimal("0.2")
f = Decimal("0.2")

result = d + e + f
print(str(result))

print("\n")

# Percentages can be calculated with floats and 100s
f_value = 0.34
p_value = f_value * 100

print(f_value, p_value)

# Simple percent function
def percent(n):
    return(str(n * 100) + "%")
print(percent(0.25))

print("\nStatistics maths ----->")
numbers = [1, 4, 17, 62, 12, 84, 5, 8, 21]

# Calculate mean
mean = statistics.mean(numbers)

# Calculate median
median = statistics.median(numbers)

# calculate mode
mode = statistics.mode(numbers)

# Calculate standard deviation
stdev = statistics.stdev(numbers)

# Print the results
print("Mean: {:f}".format(mean))
print("Median: {:f}".format(median))
print("Mode: {:f}".format(mode))
print("Standard deviation: {:f}".format(stdev))


