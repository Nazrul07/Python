# We can't directly update a tuple but we can convert it to a list, update the list, and convert it back to a tuple.
x = ("apple", "banana", "cherry")
print("Current tuple:", x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("Updated tuple:", x)
print()

## Insert Items
thistuple = ("apple", "banana", "cherry")
print("Current tuple:", thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("After insert a item updated tuple:", thistuple)
print()

## Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print("After add two tuple updated tuple:", thistuple)
print()

## Remove Items
thistuple = ("apple", "banana", "cherry")
print("Current tuple:", thistuple)
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print("After delete updated tuple:", thistuple)
print()

## Delete Tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists