"""
Based on a list of fruits, I want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension I will have to write a for statement with a conditional test inside

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "pear", "peach"]
newlist = []

for x in fruits:
  if "p" in x:
    newlist.append(x)

print(newlist)
print()

# With list comprehension I can do all that with only one line of code.
# -> Syntex: newlist = [expression for item in iterable if condition == True]
print("Using List Comprehension to filter fruits with 'p':")
newlist = [x for x in fruits if "p" in x] # fruits with letter 'p'
print(newlist)
print()

newlist = [x for x in range(10)] # numbers from 0 to 9
print(newlist)

newlist = [x for x in range(20) if x % 2 == 0 and x % 3 == 0] # even numbers divisible by 3
print(newlist)
print()

newlist = [x.capitalize() for x in fruits] # capitalizes first letter
print(newlist)

newlist = [x.upper() for x in fruits] # converts to uppercase
print(newlist)

newlist = ['hello' for x in fruits] # sets every item to 'hello'
print(newlist)
print()

print("Current List:", fruits)
newlist = [x if x != "banana" else "orange" for x in fruits]
# For every x in fruits, if x is not 'banana', keep it as it is (x), otherwise replace it with 'orange'
print("Updated List:",newlist)  
print()