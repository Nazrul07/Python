thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before adding item:", thisdict)
thisdict["color"] = "red"
print("After adding item:", thisdict)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
thisdict.update({"price": 30000})
print("After update:", thisdict)