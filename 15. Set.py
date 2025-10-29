# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, unindexed and do not allow duplicate values.
# Set items are unchangeable, but we can remove items and add new items
# Unordered means that the items in a set do not have a defined order.
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

## Simple set
myset = {"apple", "banana", "cherry"}
print(myset)

# Duplicate values will be ignored
myset = {"apple", "banana", "cherry", "apple"}
print("Set with duplicate values ignored:", myset)

# The value True is considered as 1 and False as 0. So, they treated as duplicates
thisset = {"apple", "banana", "cherry", True, False, 0, 1, 2} 
print(thisset)
print()

## Get the Length of a Set
thisset = {"apple", "banana", "cherry", "apple"} # Duplicate will be ignored and count as one item
print("The set is:", thisset)
print("The length of the set is:", len(thisset))
print()

## Set Items - Data Types
# String, int and boolean data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# A set can contain different data types
set4 = {"abc", 34, True, 40, "male"}
print(set4)
print()

## Type
myset = {"apple", "banana", "cherry"}
print(type(myset))
print()

## The set() Constructor
thisset = set(("apple", "banana", "cherry")) # tuple to set
print(thisset)

thisset = set([1, 2, 3, 4]) # list to set
print(thisset)