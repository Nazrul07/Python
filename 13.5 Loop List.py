## for loop
print("Using For Loop:")
thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
    if i < len(thislist) - 1:
        print(thislist[i], end=", ")
    else:
        print(thislist[i])

"""
# I can use this too
thislist = ["apple", "banana", "cherry"]

for index, item in enumerate(thislist):
    print(item, end=", " if index < len(thislist) - 1 else "\n")

"""

"""
Out topic: Join List
thislist = ["apple", "banana", "cherry"]
print(", ".join(thislist))

"""
# Using indexing
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i], end=", " if i < len(thislist) - 1 else "\n")
print()


## While loop
print("Using While Loop:")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i], end=", " if i < len(thislist) - 1 else "\n")
  i = i + 1
print()

## List Comprehension
print("Using List Comprehension:")
thislist = ["apple", "banana", "cherry"]
[print(x, end=", " if i < len(thislist) - 1 else "\n") for i, x in enumerate(thislist)]
# [print(x) for x in thislist]