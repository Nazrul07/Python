thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red",
  "price": 30000
}
thisdict.pop("model")     # removes item with specified key name
print(thisdict)

thisdict.popitem()        # removes the last inserted item 
print(thisdict)

del thisdict["year"]      # removes item with specified key name
print(thisdict)

# del thisdict["year"]    # raises KeyError if key not found
# thisdict.pop("model")   # raises KeyError if key not found

thisdict.clear()          # removes all items from the dictionary
print(thisdict)

del thisdict              # deletes the dictionary completely
# print(thisdict)         # raises NameError as the dictionary no longer exists