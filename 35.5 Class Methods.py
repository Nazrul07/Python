### Methods are functions that belong to a class. They define the behavior of objects created from the class.
# All methods must have self as the first parameter.

### Methods with Parameters
# Methods can accept parameters just like regular functions:
class Calculator:
  def add(self, a, b):      # Method
    return a + b

  def multiply(self, a, b): # Method
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


### Methods Accessing Properties
# Methods can access and modify object properties using self:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old."
  
p1 = Person("Nazrul", 25)
print(p1.get_info())
print()



### Methods Modifying Properties
# A method that changes a property value:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1       # Updated the original value of age.
    print(f"Happy Birthday..! You are now {self.age} years old. ")


p1 = Person("Nazrul", 24)
p1.celebrate_birthday()
print(p1.age)
print()



### The __str__() Method
# The __str__() method is a special method that controls what is returned when the object is printed:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)     # We didn't even call the __str__ function


class testing:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return f"Successfully configured for {self.name}."
  
t1 = testing("Nazrul")
print(t1)
print(t1.name)    # Also we can access manually as before