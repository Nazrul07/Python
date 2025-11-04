"""
Python Math

Python has a set of built-in math functions,
including an extensive math module,
that allows us to perform mathematical tasks on numbers.

"""
# Min, Max
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# Absolute
print(abs(-3.3))

# Power
x = pow(3,5)
print(x)

# The Math Module
import math

# The math.sqrt() method for example, returns the square root of a number
x = math.sqrt(64)
print(x)


# Floor and ceil
"""
The math.ceil() method rounds a number upwards to its nearest integer,
and the math.floor() method rounds a number downwards to its nearest integer,
and returns the result

"""
x = math.ceil(3.1)
y = math.floor(3.99)
print(x, y)


# Pi
x = math.pi
print(x)