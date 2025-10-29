"""
is 	Returns True if both variables are the same object
is not	Returns True if both variables are not the same object
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x              # z points to the same object in memory as x

print(x is z)      # True  -> because they point to the same object in memory
print(x is y)      # False -> because they are different objects in memory
print(x == y)      # True  -> The == operator checks for value equality

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)   # True -> because they are different objects in memory