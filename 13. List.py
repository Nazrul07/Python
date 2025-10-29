mylist = ["apple", "banana", "cherry"]
print(mylist)
print("Type:", type(mylist))
print("Length:", len(mylist))
print("First item:", mylist[0])
print("Last item:", mylist[-1])

# Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("List:", thislist)

# String, int and boolean data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = [1.2, 2.5, 3.6]

# A list with strings, integers and boolean values
list5 = ["abc", 34, True, 40.64, "male"]


## Using the list() constructor to make a list
thislist = list(("apple", "banana", "cherry"))
# 1. ("apple", "banana", "cherry") -> that's tuple
# 2. The list() constructor converts any iterable (like tuple, string, range, etc.) into a list.
print("Type:", type(thislist))
print("List:", thislist)