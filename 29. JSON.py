"""
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

"""
# Python has a built-in package called json, which can be used to work with JSON data.
# Import the json module
import json


## *****Parse JSON - Convert from JSON to Python*****
# If we have a JSON string, we can parse it by using the json.loads() method.
# Convert from JSON to Python

"""
Difference between JSON and Dictionary

-> JSON ≠ Dictionary (but they look alike)
-> JSON (JavaScript Object Notation) is a text format — it's just a string that stores data.
-> Python dictionary is an actual data structure in memory.

"""

# some JSON:
x = '{ "name": "Nazrul", "id":"C221019", "dep": "CSE"}'
# parse x:
y = json.loads(x)       # the result is a Python dictionary
print(type(y))
print(y)
print()


## Convert from Python to JSON -> If we have a Python object,
# We can convert it into a JSON string by using the json.dumps() method.
print(type(y))
print(y)
print()
z = json.dumps(y)       # convert to JSON
print(type(z))
print(z)                # the result is a JSON string
print()


## We can convert all of the following types to JSON
print(json.dumps({"name": "John", "age": 30}))  # Dictionary to JSON    (Object)
print(json.dumps(["apple", "bananas"]))         # List to JSON          (Array)
print(json.dumps(("apple", "bananas")))         # Tuples to JSON        (Array)
print(json.dumps("hello"))                      # String to JSON        (string)
print(json.dumps(42))                           # Integer to JSON       (number)
print(json.dumps(31.76))                        # Float to JSON         (number)
print(json.dumps(True))                         # Bool to JSON          (true)
print(json.dumps(None))                         # None to JSON          (null)
print()


x = {
  "name": "Nazrul",
  "age": 24,
  "student": True,
  "married": False,
  "interest": ("Competitve Programming", "Cyber Security"),
  "pets": None,
  "favourite_sub": [
    {"Data Structure": "4th semester", "result": 3.75},
    {"Compiler": "5th semester", "result": 4.00}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print()



## *****Format the Result*****
"""
The example above prints a JSON string, but it is not very easy to read,
with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result

"""

# Use the indent parameter to define the numbers of indents
y = json.dumps(x, indent=3)         # indent = 3 means, 3 spaces to use for indentation
print(y)
print()

"""
We can also define the separators, default value is (", ", ": "),
which means using a comma and a space to separate each object,
and a colon and a space to separate keys from values:

"""

y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)
print()


## Order the Result
# The json.dumps() method has parameters to order the keys in the result
y = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)
print(y)
print()