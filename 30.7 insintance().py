### isinstance() is one of Python’s most useful built-in functions for checking the type of a variable or object.
## isinstance(object, classinfo)
# object → the value or variable we want to check
# classinfo → the type (or tuple of types) we want to check against


# Simple type checking
x = 10
print(isinstance(x, float))
print(isinstance(x, int))


# Check for multiple types
x = 10.5
print(isinstance(x, (int, float)))  # Return ture if match to any of the defined types
print()


# Works with custom classes too!
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(d, int))