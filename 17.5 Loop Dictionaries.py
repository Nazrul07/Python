thisdic = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1954,
    "color" : "yellow",
    "price" : 20000
}

# All key
for x in thisdic:
    print(x, end = " ")
print()

# All values
for x in thisdic:
    print(thisdic[x], end = " ")
print()

# Combine
for x in thisdic:
    print("Key:", x, end = ", ")
    print("Value:", thisdic[x])
print()

# We can also use the values() method to return values of a dictionary
for x in thisdic.values():
  print(x, end = " ")
print()

# We can use the keys() method to return the keys of a dictionary
for x in thisdic.keys():
  print(x, end = " ")
print()
print()

# Both
for x, y in thisdic.items():
  print(x,":", y)
