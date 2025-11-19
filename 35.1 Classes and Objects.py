"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""

## Create a Class
class myClass:
    x = 5


#3 Create Object
p1 = myClass()
print(type(p1))
print(p1.x)     # Now, we can access the all public variable or function of the class by using the object


## Multiple Objects
p1 = myClass()
p2 = myClass()
p3 = myClass()

print(p1.x)
print(p2.x)
print(p3.x)     # We can replicate as many object as we want
#  Each object is independent and has its own copy of the class properties.


## Delete Objects
del p1
# print(p1)     # Rises an error there is no object named p1. Already deleted


## The pass Statement
# class definitions cannot be empty,
# but if we for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.

class Person:
    pass        # safe