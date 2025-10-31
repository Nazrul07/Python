"""
We cannot copy a dictionary simply by typing dict2 = dict1
Because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print("New Dictionaries:", mydict)

# Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print("New Dictionaries:",mydict)