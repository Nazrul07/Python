"""
-> Ordered
-> Can add, change, or remove items
-> Indexed
-> Allows duplicates

"""

# Updating
test = ["Nazrul", "Nazmul", "Naymul", "Nabil"]
test[1] = 3
print(test)
print()
test[1] = "Nazmul"

# Testing
print("In loop:", end=" ")
for x in test:
    print(x, end = " ")

print(test[-1])
print(test[-2])
print(test[-3])
print(test[-4])

print(test[0: 3])
print(test[-4: -1]) # -> Using netegive index we can't directly acces the 1st positive position
print()


# Adding
test.append("Nahian")
print(test)
print()

# Deleting
print("Before removing Naymul: ",test)
test.remove("Naymul") # remove by value
print("After removing Naymul: ",test)
print()

print("Before poping 1st position: ",test)
test.pop(1) # remove by index
print("After poping: ",test)
print()

# Shorting
print("Before sorting: ", test)
test.sort()
print("Aefore sorting: ", test)
print()

# Reversing
print("Before reversing: ", test)
test.reverse()
print("Aefore reversing: ", test)
print()

# Copying
test2 = test.copy()
print(test2)