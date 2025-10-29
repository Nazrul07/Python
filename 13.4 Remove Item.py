thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # The remove() method removes the specified item.
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "banana"]
thislist.remove("banana") # The remove() method removes the first occurrence of the specified item.
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # The pop() method removes the specified index, (or the last item if index is not specified).
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() # Remove the last item
print(thislist)
print()

# The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
# del "apple"  # This will raise an error
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist  # Delete the entire list
# print(thislist)  # This will raise an error because the list no longer exists

thislist = ["apple", "banana", "cherry"]
thislist.clear() # The clear() method empties the list but keeps the list itself.
print(thislist)

thislist = ["apple", "banana", "cherry"]
# thislist.pop(1:2) # This will raise an error because pop() does not support slicing

# Delete multiple items using slicing with del
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("Current List:", thislist)
del thislist[1:4]  # Deletes items at index 1, 2, and 3
print("Updated List:", thislist)
print()

# Using list slicing assignment to remove multiple items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("Current List:", thislist)
thislist[1:4] = []  # Removes items at index 1, 2, and 3
print("Updated List:", thislist)