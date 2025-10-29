## Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # Add "orange" at the end of the list
print(thislist)
print()

## Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # Insert "orange" at index 1(0 based index)
print(thislist)
print()

## Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical[:2]) # Extend list by adding first two items of tropical list
print(thislist)

# The extend() method does not have to append lists, It can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)