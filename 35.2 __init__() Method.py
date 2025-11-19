### The __init__() Method
# -> All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
# -> The __init__() method is used to assign values to object properties,
# or to perform operations that are necessary when the object is being created.


### Create a class named Person, use the __init__() method to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Nazrul", 24)

print("Name:",p1.name)
print("Age:",p1.age)
print()

# The __init__() method is called automatically every time the class is being used to create a new object.



### Without the __init__() method
class Person_:
    pass

ps1 = Person_()
ps1.name = "Tobias"
ps1.age = 24

ps2 = Person_()
ps2.name = "Yasir"
ps2.age = 25

print(ps1.name)
print(ps1.age)

print(ps2.name)
print(ps2.age)
# Here without __init()__ function we will need to define again again manually for each object we create.
# So, To reduce the code and increase readability we use __init()__ to solve the problem.



### Default Values in __init__()
class Person:
    def __init__(self, name, age = 24):
        self.name = name
        self.age = age

person1 = Person("Nazrul")      # Use the default value
person2 = Person("Yasir", 25)

print(f"First person is {person1.name} and he is {person1.age} years old.")
print(f"Second person is {person2.name} and he is {person2.age} years old.\n")



### Multiple Parameters
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

person1 = Person("Nazrul", 24, "Cumilla", "Bangladesh")

print(f"His name is {person1.name}. He is {person1.age} years old. He is from {person1.city} of {person1.country}.")