"""
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.

"""

# Creating a Function -> A function is defined using the def keyword
#Note: A function in Python does not execute automatically when we create (define) it — it only runs when we call it.
def greet():
    print("Hello from a function")

# Function is defined but not executed yet

greet()  # Function executes only when called
# I can call multiple of time if I want to execute the function.


"""
Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)

vaild function names example:
calculate_sum()
_private_function()
myFunction2()

"""

"""
Why Use Functions?
-> Function is used to reduce the code repeatation, reusable and increase readability.

Without functions - repetitive code:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

With functions - reusable code:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

-> Simple isn't it?
"""

## Return Values
# -> Functions can send data back to the code that called them using the return statement.
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# or we can use the returned value directly
def get_greeting():
  return "Hello from a function"

print(get_greeting())

# If a function doesn't have a return statement, it returns None by default.


## The pass Statement
# Function definitions cannot be empty. If We need to create a function placeholder without any code, use the pass statement.
def my_function():
  pass

# The pass statement is often used when developing, allowing us to define the structure first and implement details later.