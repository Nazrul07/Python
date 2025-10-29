## Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange") # adds 'orange' at the end
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)      # adds list b as a single element at the end of list a
print(a)
print(a[3])      # prints the appended list
print(a[3][0])   # prints the first element of the appended list
print()

## Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)
print()

## 	Returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
x = fruits.copy()
print(x)

## 	Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print("Number of 'cherry' in the list:", x)
print()

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print("Number of 9's in the list:", x)
print()

## Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)
print(fruits)

## Returns the index of the first element appearance with the specified value
fruits = ['apple', 'banana', 'cherry', 'banana']
x = fruits.index("banana") # the index() method returns the position at the first occurrence of the specified value
print("Index of 'banana' in the list:", x)
print()

# list.index(elmnt, start, end)
points = [1, 2, 3, 4, 3, 5, 3]
x = points.index(3, 3, 6) # find the index of 3, starting from index 3 to index 6
print("Index of 3 between index 3 and 6:", x)

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print("Index of 32 in the list:", x)
print()

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4) # Find the position of 'cherry', but start the search at position 4
print(x)

## 	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange") # inserts 'orange' at index 1
print(fruits)
print()

## 	Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1) # removes the element at index 1
print(fruits)
print()

## 	Removes the item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("cherry") # removes the first occurrence of 'cherry'
print(fruits)
print()

## Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()    # reverses the list
print(fruits)
print()

## Sorts the list
fruits = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
fruits.sort()      # sorts the list in ascending order
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True) # sorts the list in descending order
print(cars)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc) # sorts the list based on the length of the values
print(cars)


# A function that returns the 'year' value:
def myFunc(e):
  return e["year"]
cars = [
  {"car": "Ford", "year": 2005},
  {"car": "Mitsubishi", "year": 2000},
  {"car": "BMW", "year": 2019},
  {"car": "VW", "year": 2011}
]

cars.sort(key=myFunc)
print(cars)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc) # Sort the list by the length of the values and reversed
print(cars)