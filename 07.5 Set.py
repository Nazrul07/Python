"""
-> Used to store unordered, unique elements.

"""

fruits = {"apple", "banana", "cherry", "apple"} # duplicate will automatically delete
print(fruits)
print()

# add
fruits.add("orange")
print(fruits)
print()

# delete
fruits.remove("cherry")
print(fruits)

# fruits.remove("banana")   # ❌ Error if not found
# OR safely:
# fruits.discard("banana")  # ✅ No error if not found

# fruits.clear()  # removes all items
# del fruits      # deletes the set

# print(fruits[0])  # ❌ Error

for fruit in fruits:
    print(fruit, end = " ")
print()
print()


# Set operation
a = {1, 2, 3, 5, 9}
b = {2, 4, 6}

print(a | b) # Set union
print(a & b) # Intersection
print(a - b) # Difference
print(a ^ b) # Symmetric difference (not common)


# x = {}         # This is an empty DICTIONARY
# x = set()      # This is an empty SET