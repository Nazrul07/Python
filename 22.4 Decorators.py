## *****Python Decorators*****
"""
Decorators let us add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.

"""

## Basic Decorator
# Define the decorator first, then apply it with @decorator_name above the function.


# A basic decorator that uppercases the return value of the decorated function.
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunc():
    return "Hello Nazrul"

"""
same as,
def myfunc():
    return "Hello Nazrul"

myfunc = changecase(myfunc)

"""
print(myfunc())
print()


# Multiple Decorator Calls
def decorator(fun):
    def myinner():
        return fun().upper()
    return myinner

@decorator
def fun1():
    return "Hello World..!"

@decorator
def fun2():
    return "This is modern era."

print(fun1())
print(fun2())
print()


## Arguments in the Decorated Function
# Functions that requires arguments can also be decorated, just make sure we pass the arguments to the wrapper function:
def decorator(func):
    def inner(x):
        return func(x).upper()
    return inner

@decorator
def fun(name):
    return "Hello " + name

print(fun("Nazrul"))
print()


# Modify only to the argument
def decorator(func):
    def inner(x):
        return func(x.upper())
    return inner

@decorator
def fun(name):
    return "Hello " + name

print(fun("Nazrul"))
print()



## *args and **kwargs
"""
Sometimes the decorator function has no control over the arguments passed from decorated function,
to solve this problem, add (*args, **kwargs) to the wrapper function, 
this way the wrapper function can accept any number, 
and any type of arguments, and pass them to the decorated function.

"""
def decorator(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return inner

@decorator
def fun(name):
    return "Hello " + name

print(fun("Nazrul"))
print()



# A decorator factory that takes an argument and transforms the casing based on the argument value.
def changecase(n):
    def decorator(func):
        def inner(*args, **kwargs):
            if n == "upper":
                return func(*args, **kwargs).upper()
            else:
                return func(*args, **kwargs).lower()
        return inner
    return decorator

@changecase("upper")
def fun(name):
    return "Hello " + name

print(fun("Nazrul"))
print()


# Another example
def changecase(n):
    def decorator(func):
        def innerfun(x = "Guest"):
            if n == 1:
                return func(x.upper())
            else:
                return func(x.lower())
        return innerfun
    return decorator
        


@changecase(1)
def greeting(name = "Guest"):
    return "Hello " + name

print(greeting("Nazrul"))
print(greeting())
print()



## Multiple Decorators
"""
We can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.

"""
def addgreeting(func):
    def inner():
        return "Hello " + func() + " Have nice day...!"
    return inner


@addgreeting
def fun():
    return "Nazrul"

print(fun())
print()


"""
What is function metadata?
-> Every function in Python is an object, and it carries some metadata — basically, information about the function itself.
__name__	     ->  The name of the function
__doc__	         ->  The docstring (documentation) of the function
__module__       ->	 The module (file) name where it was defined

"""
def myfunction():
    return "Have a great day!"

print(myfunction.__name__)   # function’s name
print(myfunction.__doc__)    # function’s documentation
print(myfunction.__module__) # Where it's defined
print()



def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)   # function’s name
print(myfunction.__doc__)    # function’s documentation
print(myfunction.__module__) # Where it's defined
print()


# Import functools.wraps to preserve the original function name and docstring.
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)