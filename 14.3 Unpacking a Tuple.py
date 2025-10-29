"""
When we create a tuple, we normally assign values to it. This is called "packing" a tuple

"""

# Packing a tuple
thistuple = ("apple", "banana", "cherry")
print("Packed tuple:", thistuple)

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
x, y, z = fruits

print(x)
print(y)
print(z)
x1 = x + ' ' + y
print("Concatenated string:", x1)
print()

num_tuple = (1, 2, 3)
a, b, c = num_tuple
print("Sum of numbers:", a + b + c)

## Using Asterisk*
# -> If the number of variables is less than the number of values, we can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)

(*green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()