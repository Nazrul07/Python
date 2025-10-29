thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1]) # access item at index 1
# The first item has index 0.

## Negative Indexing
print(thistuple[-1]) # access last item
print(thistuple[-3]) # access third last item
print()

## Range of Indexes
print(thistuple[0:4]) # access items from index 0 to 4
print(thistuple[2:5]) # access items from index 2 to 5
print(thistuple[:4])  # access items from start to index 4
print(thistuple[2:])  # access items from index 2 to end
print()

## Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # access items from index 4th to 6th
print(thistuple[-6:-2]) # access items from index 2nd to 5th
print(thistuple[-5:])   # access items from index 3rd to end
print(thistuple[:-3])   # access items from start to index 4th
print()

## Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")