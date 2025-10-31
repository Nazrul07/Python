## clear() -> Removes all the elements from the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

print(car)



## copy() -> Returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car1 = car.copy()
print(car1)



## fromkeys() -> Returns a dictionary with the specified keys and value
x = ("Orane", "Mango", "Apple")
y = (0)
thisdict = dict.fromkeys(x,y) # Assigining one vlaue to every key
print(thisdict)
print()

x = ("Orane", "Mango", "Apple")
y = (0, 2)
thisdict = dict.fromkeys(x,y) # Assigining two vlaues to every key
print(thisdict)
print()

x = ("Orane", "Mango", "Apple")
thisdict = dict.fromkeys(x) # empty key
print(thisdict)



## get() -> Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)
print(car["year"]) # we can use both

print(car.get("year", 1970)) # Already assigned value will be print, if the key does't exist then the new value will be print
x = car.get("price", 20000) # If the item is not exist in the dictionaries then the current assign value will be print
print(x)
print()



## items() -> Returns a list containing a tuple for each key value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items() # Means both now share the same memory address. If we change anything in the original dictionary view object will get effect.
print("After copying:",x)

car["price"] = 20000
print("After changing in other dictionary:",x)
print()



## keys() -> Returns a list containing the dictionary's keys
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
# The view object will reflect any changes done to the dictionary
# It's dynamic
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print("After just copying:",x)
car["color"] = "Red"
print("Changing in the dictionary. Then",x)



## pop() -> Removes the element with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Original Dictionary:",car)
car.pop("year")
print("After deleting 'year' :",car)

# Another example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.pop("model") # The value of the removed item is the return value of the pop() method
print(x)
print()



## popitem() -> Removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem() # So, year will be delete
print(car)

# We can store the removed value. The removed item is the return value of the popitem() method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.popitem()
print(x)
print()



## setdefault()	-> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# If the key exist, this parameter has no effect.
# If the key does not exist, this value becomes the key's value. And the key and value will be updated to the original dictionary.
x = car.setdefault("model", "Bronco") # "model" was already defined. So the previous value will be displayed.
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x)
print(car)
print()



## update() -> Updates the dictionary with the specified key-value pairs.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color" : "white"})
print(car)

car.update({"year" : "1960"})
print(car)

# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object with key value pairs.

fruits_dict = {
    "Banana" : "2kg",
    "Malon" : "2kg"
}
fruits_dict.update({"Orange" : "1kg", "Mango" : "1.5kg"})
print(fruits_dict)

fruits_dict.update([("Jack Fruits", "1pic"), ("Apple", "2kg")]) # Tuples
print(fruits_dict)
print()


## values() -> Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)

# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
# The view object will reflect any changes done to the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018 # When a values is changed in the dictionary, the view object also gets updated.

print(x)