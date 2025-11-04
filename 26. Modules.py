"""
Module

Consider a module to be the same as a code library.
A file containing a set of functions we want to include in our application.

The module can contain functions,
but also variables of all types (arrays, dictionaries, objects etc)

Created a module named mymodule.py
"""


# Use a Module named mymodule
import mymodule
mymodule.greeting("Nazrul")  # When using a function from a module, use the syntax: module_name.function_name.

a = mymodule.person1         # We can directly access everything that is containing the module just by importing the module
print(a)


"""
Naming a Module:
WE can name the module file whatever we like, but it must have the file extension .py

Re-naming a Module:
We can create an alias when we import a module, by using the as keyword

"""

import mymodule as mx

a = mx.person1["id"]
print(a)
print()


## *****Built-in Modules*****
# There are several built-in modules in Python, which we can import whenever we like
import platform as pf
x = pf.system()
print(x)
print()


# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
x = dir(mymodule)
print(x)
print()


## Import From Module
# We can choose to import only parts from a module, by using the from keyword
from mymodule import person1  # just for specific, expect that we can't access other functions

print(person1["id"])          # When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
