# A tuple is a collection which is ordered and unchangeable
# -> Tuple items are ordered, unchangeable, and allow duplicate values.
# -> Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

mytuple = ("apple", "banana", "cherry")
print(mytuple)

## Allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("Length of the tuple:", len(thistuple))
print("Tuple items:", thistuple)

## Create Tuple With One Item
thistuple = ("apple",) # note the comma
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print()

## Data Types

# -> Tuples can contain different data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
t = 1, 2, 3 # We can create a tuple without parentheses, using just commas.
# Parentheses are optional except when needed for grouping or empty tuples.

print(type(t))  # <class 'tuple'>
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(tuple1)
print(tuple2)
print(tuple3)

# -> A tuple can contain different data types
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)


## The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

new_tuple = tuple([1, 2, 3, 4]) # list to tuple
print(new_tuple)