# Sorting a List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sorting a List Numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # Sort the list based on how close the number is to 50
print(thislist)
print()

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() # By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
print(thislist)

# Perform a case-insensitive sort of the list
thislist = ["banana", "orange", "Kiwi", "Cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
thislist = ["banana", "orange", "Kiwi", "Cherry"]
thislist.reverse() # Reverses the current order of the list, it does not sort the list in descending order.
print(thislist)