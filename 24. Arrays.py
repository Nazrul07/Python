"""
Python does not have built-in support for Arrays, but Python Lists can be used instead.

"""
# Arrays are used to store multiple values in one single variable. Let we have some variable look like:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
# However, what if we want to loop through the cars and find a specific one?
# And what if we had not 3 cars, but 300?
# To solve this kind of problem, we use array.
# An array can hold many values under a single name.Like:
cars = ["Ford", "Volvo", "BMW"]

# We can access any element from the list just my referring to index number.
print(cars[1])          # Volvo
print(cars[0])          # Ford

# We can edit them,
cars[0] = "Toyota"
print(cars)             # Modify the value of the first array item 

# Lenght 
print(len(cars))

# Looping Array Elements
for x in cars:
    print(x, end = " ")
print()

# Adding Array Elements
cars.append("Honda")
print(cars)
print()

# pop()   -> Removing Array Elements
print("Before delete:",cars)
cars.pop(1)             # Delete by index
print(cars)

cars.remove("Honda")    # By item
print(cars)

# copy()  -> Returns a copy of the list
new_list = cars.copy()
print(new_list)

# clear() -> Removes all the elements from the list
new_list.clear()
print(new_list)

# count()  -> Returns the number of elements with the specified value
num = [1, 2, 3, 1, 2, 1]
cnt = num.count(1)
print(cnt)

# extend()  -> Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)     # Adding the cars list after the fruits list
print(fruits)
print()

# index()	-> Returns the index of the first element with the specified value
fruits = ['cherry','apple', 'banana', 'cherry']

x = fruits.index("cherry") # first apperence
print(x)

# insert()	-> Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")    # adding as second element
print(fruits)


# remove()	-> Removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
print(fruits)
print()

# reverse()	 -> Reverses the order of the list
num = [1, 3, 2, 10, 3, 3, 5, 1]
num.reverse()       # just reverse the order
print(num) 

# sort()      -> Sorts the list - increasing
num.sort()
print(num)

# reverse sort 
num = [1, 3, 2, 10, 3, 3, 5, 1]
num.sort(reverse=True)   # Sorting in reverse order
print(num)