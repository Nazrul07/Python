# Information can be passed into functions as arguments.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# *****Parameters vs Arguments*****

"""
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

"""

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


# *****Number of Arguments*****
# By default, a function must be called with the correct number of arguments.
# If our function expects 2 arguments, we must call it with exactly 2 arguments. If 1, then 1. Must be same.

def my_function(fname, lname):
  print(fname + " " + lname)
print()

my_function("Emil", "Refsnes")

"""
Wrong 

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

"""


# *****Default Parameter Values*****
# We can assign default values to parameters. If the function is called without an argument, it uses the default value.
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
print()


## We can send arguments with the key = value syntax

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
print()

my_function(name = "Buddy", animal = "dog") # This way, with keyword arguments, the order of the arguments does not matter.
print()


# *****Positional Arguments*****
# When we call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order to get the expected output

my_function("dog", "Buddy")
print()
# my_function("Buddy", "dog") # This still work but due to swtching the order or misplace the order we won't get the expect output as we want.


## Mixing Positional and Keyword Arguments
# We can mix positional and keyword arguments in a function call.
# However, positional arguments must come before keyword arguments.

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
# my_function(name = "Buddy", "dog" , age = 5) # ❌ Positional argument ("dog") follows keyword argument (name="Buddy")

# All positional
my_function("dog", "Buddy", 5)

# All keyword
my_function(animal="dog", name="Buddy", age=5)

# Keyword arguments only after positional
my_function("dog", name="Buddy", age=5)
my_function("dog", age = 5, name = "Buddy") # Still work, because it follows the rule

"""
my_function("dog", "Buddy", name = "Tiger") 

animal = "dog" (positional)

name = "Buddy" (positional)

then name = "Tiger" (keyword) ← conflict ❌

"""


# *****Passing Different Data Types*****
"""
We can send any data type as an argument to a function (string, number, list, dictionary, etc.).

The data type will be preserved inside the function:

"""
def my_function(fruits):
  for fruit in fruits:
    print(fruit, end = " ")

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) # Sending list as an argument
print()

# Sending a dictionary as an argument
def my_function(person):
  print("Name:", person["Name"])
  print("Age:", person["Age"])

my_person = {"Name": "Nazrul", "Age": 25}
my_function(my_person)



# *****Return Values*****
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


# Returning List
def my_function():
  return ["Provat", "Hasan", "Yasir"]

my_friends = my_function()
print(my_friends)

# A function that returns a tuple
def my_function():
  return (10, 20)

a, b = my_function()
print(a,b)