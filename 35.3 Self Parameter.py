# The self parameter is a reference to the current instance of the class.

# It is used to access properties and methods that belong to the class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

p1 = Person("Nazrul", 25)
p1.greet()
print()

# The self parameter must be the first parameter of any method in the class.




"""
Why Use self?
Without self, Python would not know which object's properties we want to access

"""
# The self parameter links the method to the specific object:
class Person:
    def __init__(self, name):
        self.name = name
    
    def printname(self):
        print(self.name)

p1 = Person("Hasan")
p2 = Person("Sayem")

p1.printname()
p2.printname()
print()



## self Does Not Have to Be Named "self"
# It does not have to be named self, we can call it whatever we like, but it has to be the first parameter of any method in the class:
class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age
    
    def greet(abc):
        print(f"Hello, my name is {abc.name} and I'm {abc.age} years old.")


p1 = Person("Nazrul", 24)
p1.greet()
print()

# While we can use a different name, it is strongly recommended to use self as it is the convention in Python and makes code more readable to others.




### Accessing Properties with self
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()



### Calling Methods with self
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return "Hello " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "!. Welcome to our website.")

p1 = Person("Nazrul")
p1.welcome()