# Properties are variables that belong to a class. They store data for each object created from the class.

# Create a class with properties:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Emi", 23)
print(p1.name)
print(p1.age)



### Access Properties
# Access the properties of an object:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)
print()



### Modify Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(Person)
print(p1)
print(p1.age)
p1.age = 26

print(p1.age)
print()



### Delete Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age  # Delete for p1 object not for the whole class

print(p1.name) # This works
# print(p1.age) # This would cause an error



### Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
class Person:
   a = 10
   def __init__(self, name):
      print("Hello " + name)

p1 = Person("Nazrul")
p2 = Person("Islam")
print(p1.a)
print(p2.a)     # both same
print()


### Modifying Class Properties
# Modifying Class Properties:
class Person:
  lastname = "None"

  def __init__(self, name):
    self.name = name

p1 = Person("Saiful")
p2 = Person("Nazrul")

print(p1.lastname)
Person.lastname = "Islam"   # If I modify the value of a class properties it will change for all of the object that may define after that.
print(p1.lastname)
print(p2.lastname)
print()



### Add New Properties
# We can add new properties to existing objects:
class Person:
   def __init__(self, name):
      self.name = name
    
p1 = Person("Nazrul")
p1.age = 24     # Although the class have no variable like age, city but we can add for the object
p1.city = "Cumilla"

print(p1.name)
print(p1.age)
print(p1.city)


p2 = Person("Hasan")
print(p2.name)
# print(p2.age) # Error because there is no age variable for p2. For p1 we just defined it additionally.

# Adding properties this way only adds them to that specific object, not to all objects of the class.