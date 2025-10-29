# We cannot access items in a set by referring to an index or a key.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x, end = " ")
print()

print("banana" in thisset) # Check if "banana" is present in the set

print("orange" not in thisset) # Check if "orange" is NOT present in the set