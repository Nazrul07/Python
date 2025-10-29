list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
list1[0] = "x"
print(list3)
print(list1)

# Confusion clearification
list1 = ["a"]
list2 = list1            # Share memory reference
list3 = list1 + list2    # New list created in different memory location

print("Id of list1:", id(list1))
print("Id of list2:", id(list2))
print("Id of list3:", id(list3))

# Another way to join two lists is by appending all the items from list2 into list1, one by one
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Or we can use the extend() method, which purpose is to add elements of a list (or any iterable), to the end of the current list.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
