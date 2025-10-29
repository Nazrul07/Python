## Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print()

## Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["watermelon"] # Change the 2nd and 4th value by replacing it with one value
print(thislist)

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']  # Change "banana" by replacing it with "kiwi" and "mango"
print(mylist)
print()

## Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # Insert "watermelon" at index 2(0 based index)
print(thislist)
print()