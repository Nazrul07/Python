# Add Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") # Use the add() method to add an item to a set at the end.

print(thisset)

# To add items from another set into the current set, use the update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
print("Thisset set:", thisset)
print("Tropical set:", tropical)
thisset.update(tropical) # Order unpredictable, as sets are unordered collections

print("Updated Thisset set:", thisset)
print()

## Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"] # list
thisset.update(mylist)

print("Updated Thisset set:", thisset)