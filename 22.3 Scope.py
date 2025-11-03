# A variable is only available from inside the region it is created. This is called scope.

## Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

from tkinter import Variable


def myfunc():
  x = 300
  print(x)

myfunc()
# print(x) # Error -> We can't access the variable from outside of the function. It only be used in the function where it is created.


# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function.
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
print()


## Global Scope
# A variable created in the main body of the code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
print()


## Naming Variables
# If we operate with the same variable name inside and outside of a function,
# Python will treat them as two separate variables,
# one available in the global scope (outside the function) and one available in the local scope(inside the function)
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
print()



## Global Keyword
# If we need to create a global variable, but are stuck in the local scope,
# we can use the global keyword.
# The global keyword makes the variable global.

x = 300

def my_fun():
  global x # Any changes in the function for x, will effect on global variable
  x = 200  # Now global variable is updated
  print(x)

my_fun()
print(x, "\n")



## Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the Variable belong to the outer function.
def myfun1():
  x = 24
  def myfun2():
    nonlocal x
    x = 20
  myfun2()
  return x

print(myfun1())



## The LEGB Rule
"""
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace

"""
# Ex - 01
x = 10

def myfun():
  x = 20
  def myfun1():
    x = 25
    print("Local:",x)
  myfun1()
  print("Enclosing:",x)

myfun()
print("Global:",x)
print()


# Ex - 02
x = 10

def myfun():
  x = 20
  def myfun1():
    print("Enclosing:",x)

  myfun1()
  print("Enclosing:",x)

myfun()
print("Global:",x)
print()


# Ex - 03
x = 10

def myfun():
  def myfun1():
    print("Global:",x)
    
  myfun1()
  print("Global:",x)

myfun()
print("Global:",x)