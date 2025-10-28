## Return true or false

print(10 > 9)
print(9 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")

# -> Almost any value is evaluated to True if it has some sort of content.
# -> Any string is True, except empty strings.
# -> Any number is True, except 0.
# -> Any list, tuple, set, and dictionary are True, except empty ones.
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# These are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# -> One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# -> Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# -> isinstance() function, which can be used to determine if an object is of a certain data type or not
p = True
x = 200
y = 200.5
z = 3 + 5j
print(isinstance(x, int))
print(isinstance(y, float))
print(isinstance(z, complex))

if p:
  print("P is boolean")
else:
  print("P is not boolean")