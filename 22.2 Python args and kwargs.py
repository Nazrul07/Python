# ******args and **kwargs*****
"""
By default, a function must be called with the correct number of arguments.

However, sometimes we may not know how many arguments that will be passed into our function.

*args and **kwargs allow functions to accept a unknown number of arguments.

"""

# Arbitrary Arguments - *args
"""
If we do not know how many arguments will be passed into our function, we add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly

"""

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print()
# The *args parameter allows a function to accept any number of positional arguments.


# Using *args with Regular Arguments
# We can combine regular parameters with *args

def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Nazurl", "Yasir", "Hasan")


def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total 

print(my_function(1, 3, 5))
print(my_function(10, 20, 30, 40))
print(my_function(5))


# Arbitrary Keyword Arguments - **kwargs
"""
If we do not know how many keyword arguments will be passed into our function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly.

"""

# Using **kwargs to accept any number of keyword arguments

def my_function(**kid):
  print("His last name is " +kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["Name"])
  print("Age:", myvar["Age"])
  print("All data:", myvar)

my_function(Name = "Nazrul", Age = 25, City = "Cumilla")

# Using **kwargs with Regular Arguments

def my_function(username, ** details):
  print("Username:",username)
  print("Additional Details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("Nazrul07", fname = "Nazrul", lname = "Islam", Age = 25, City = "Cumilla")


## Combining *args and **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def my_fun(title, *args, **kwargs):
  print("Title:",title)
  print("Full Name: ", args[0],args[1])
  for key, value in kwargs.items():
    print(key + ":",value)

my_fun("User Info", "Nazrul", "Islam", Age = 25, Department = "CSE", Section = "A")


## Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
# If we have values stored in a list, we can use * to unpack them into individual arguments
def my_function(a, b, c):
  return a+b+c
  
numbers = [1, 2, 3]
result = my_function(*numbers)
print(result)



def my_fun(fname, lname):
  print("Hello",fname,lname)
  
person = {"fname": "Emil", "lname": "Refsnes"}
my_fun(**person)