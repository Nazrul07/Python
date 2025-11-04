"""
*****Iterators*****

An iterator is an object that contains a countable number of values.
That can be iterated upon, meaning that we can traverse through all the values.

"""


"""
*****Iterator vs Iterable*****
Lists, tuples, dictionaries, and sets are all iterable objects.
They are iterable containers which we can get an iterator from.

"""

# All these objects have a iter() method which is used to get an iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))   # last item
# print(next(myit)) # rise an error -> StopIteration. Becasue there is no other item.
print()


# for string -> string also iterable
mystr = "Bangladesh"
myit = iter(mystr)
print(next(myit))
print(next(myit))


# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x, end = " ")
print()


mystr = "banana"

for x in mystr:
  print(x, end = " ")
print()



"""
*****Create an Iterator*****
To create an object/class as an iterator,
We have to implement the methods __iter__() and __next__() to our object.

The __iter__() method ->
We can do operations (initializing etc.),
but must always return the iterator object itself.


The __next__() method ->
Also allows us to do operations,
and must return the next item in the sequence.
"""

class myNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a +=1
    return x
  
myclass = myNumbers()       # This creates an instance of the class MyNumbers
myiter = iter(myclass)      # looks for a method named __iter__() inside the class.

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print()


# StopIteration
class myNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 10:
        x = self.a
        self.a +=1
        return x
    else:
      raise StopIteration
  
myclass = myNumbers()       # This creates an instance of the class MyNumbers
myiter = iter(myclass)      # looks for a method named __iter__() inside the class.

for x in myiter:
  print(x, end = " ")
print()

"""
# 1. Get an iterator from myiter
iterator = iter(myiter)

# 2. Loop manually using next()
while True:
    try:
        x = next(iterator)   # calls your __next__() method
        print(x, end=" ")
    except StopIteration:     # automatically catches the StopIteration exception
        break                 # ends the loop

"""