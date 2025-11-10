# None is a special constant in Python that represents the absence of a value.
# Its data type is NoneType, and None is the only instance of a NoneType object.

x = None
print(x)
print(type(x))


result = None
if result is None:
    print("No result yet")
else:
    print("Result is Ready")


# None evaluates to False in a boolean context.
print(bool(None))


# Functions that do not explicitly return a value, return None by default.
def myfun():
    x = 5

x = myfun()
print(x)
