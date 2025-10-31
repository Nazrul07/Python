thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model") # same as thisdict["model"]
print(x)

x = thisdict.keys() # returns a view object that displays a list of all the keys in the dictionary.
print(x)

x = thisdict.values() # returns a view object that displays a list of all the values in the dictionary.
print(x)

# Add a new item to the original dictionary
thisdict["color"] = "red"
print(thisdict) # The view object will reflect the changes

# We can change values of existing keys
thisdict["year"] = 2020
print(thisdict)

# Get Values
x = thisdict.values()
print(x)
print()

# Check if Key Exists
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "color" : "red"
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


if "price" in thisdict:
    print("Yes, 'price' is one of the keys in the thisdict dictionary")
else:
    print("No, 'price' key does not exist in thisdict dictionary")