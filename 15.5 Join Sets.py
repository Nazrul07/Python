"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

"""

## The union() method returns a new set with all items from both sets. --> OR Operation
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "c"}
set3 = set1.union(set2) # No duplicates
# set3 = set2.union(set1) # Order does not matter
print(set3)


# We can use the | operator instead of the union() method, and we will get the same result.
set4 = set1 | set2
print(set4)
print()


# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)


# myset = set1 | set2 | set3 | set4 # Using the | operator
print("Updated set:", myset)
print()


# Join a Set and a Tuple
set5 = {"x", "y", "z"}
tuple1 = ("apple", "banana", "cherry")

myset = set5.union(tuple1)
print("Updated set:", myset)



## The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)

print(set1)
print()



## Intersection --> AND Operation
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"a", "b", "c", 1, 2, 3}
set2 = {1, 2, 3, "c", "d", "e"}
set3 = set1.intersection(set2)
# set2.intersection(set1) -> this will not change the result, we need to store the changes
# print(set2)
print("Intersection set:", set3)


# We can use the & operator instead of the intersection() method, and we will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2 # The & operator only allows us to join sets with sets, and not with other data types like we can with the intersection() method.
print(set3)


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"a", "b", "c", 1, 2, 3}
set2 = {1, 2, 3, "c", "d", "e"}
set1.intersection_update(set2)
print("Updated set1 after intersection_update:", set1)
print()


# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)

print(set3)