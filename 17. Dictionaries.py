"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))
print(thisdict.values()) # returns a view object that displays a list of all the values in the dictionary.
print(thisdict.keys())   # returns a view object that displays a list of all the keys in the dictionary.

# Duplicate values will overwrite existing values or with last occurance value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict)) # length of dictionary

# We can use list inside dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

print(thisdict["colors"])
print(type(thisdict))

# The dict() Constructor -> It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)