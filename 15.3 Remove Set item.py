# Remove Set Items
## To remove an item in a set, use the remove(), or the discard() method.

# Using remove()
thisset = {"apple", "banana", "cherry"}
print("Original set:", thisset)
thisset.remove("banana")     # Remove "banana" from the set
print("Set after remove 'banana':", thisset)
print()

# Using discard()
newSet = {"orange", "kiwi", "melon"}
print("Original newSet:", newSet)
newSet.discard("kiwi")       # Discard "kiwi" from the set
print("NewSet after discard 'kiwi':", newSet)
print()

# Remove a random item by using the pop() method
thisset = {"apple", "banana", "cherry", "melon"}
print("Original set:", thisset)
thisset.pop() # Remove a random item
print("Set after pop an item:", thisset)
print()

# Remove all items by using the clear() method
thisset = {"apple", "banana", "cherry"}
thisset.clear()  # Remove all items
print(thisset)
print()

# The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # this will raise an error because the set no longer exists