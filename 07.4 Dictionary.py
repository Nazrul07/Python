"""
Directory store values as pair

dictionary = {
    key1: value1,
    key2: value2,
    key3: value3
}

-> Key must unique
-> faster - use hash table
-> flexible
-> readable
-> dynamic

"""

person = {
    "name": "John",
    "age": 36,
    "country": "USA"
}

# showing
print("Name:", person["name"])
print("Age: ", person.get("age"))  # We have to use .get to get the value of the key
print()

# adding
person["email"] = "nazrul103n@gmail.com"

# updating
person["age"] = 25

#delete
del person["country"]

print(person)
print()

# person = {key.capitalize(): value for key, value in person.items()}
for key, value in person.items():
    print(key.capitalize(), ":", value) # Capitalize only the 1st character of the key 

