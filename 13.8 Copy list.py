"""
We cannot copy a list simply by typing list2 = list.
Because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2

"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
thislist.append("orange")
print("Original list:", thislist)
print("New list:", mylist)
print()

# Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print("New list:", mylist)
print()

# Slice Operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
thislist.append("Orange")
print("New list:", mylist)
