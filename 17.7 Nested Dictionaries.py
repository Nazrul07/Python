myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Another way
child1 = {
    "name" : "Emil",
    "year" : 2004
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

child3 = {
    "name" : "Linus",
    "year" : 2011
}

myFamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myFamily)
print()

# Accessing the dictionaries
print(myFamily["child1"]["name"])
print(myFamily["child3"]["year"])
print()

# Loop Through Nested Dictionaries
for x, object in myFamily.items():
    print(x + ":")
    for key, value in object.items():
        print(f"  {key}: {value}")
