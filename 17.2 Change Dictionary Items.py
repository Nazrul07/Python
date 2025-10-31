# We can change the value of a specific item by referring to its key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before change:", thisdict)
thisdict["year"] = 2018
print("After change:", thisdict)

# The update() method will update the dictionary with the items from the given argument.
thisdict.update({"year": 2020, "color": "red"})
print("After update:", thisdict)