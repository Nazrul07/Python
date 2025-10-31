# A for loop is used to go through each item in a sequence (like a list, tuple, set, or string) and run code for each item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x, end = " ")
print()

# Looping Through a String
for x in "Original":
  print(x, end = "")
print()

# The break Statement -> With the break statement we can stop the loop before it has looped through all the items.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x, end = " ")
  if x == "banana":
    break
print()

# The continue Statement -> With the continue statement we can stop the current iteration of the loop, and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x, end = " ")
print()

# The range() Function -> The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# We don't need extra variable to run the loop

for x in range(6):
  print(x, end = " ")
print()

for x in range(2, 6): # which means values from 2 to 6 (but not including 6)
  print(x, end = " ")
print()


# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 30, 3): # Increment the sequence with 3
  print(x, end = " ")
print()

# Else in For Loop
for x in range(6):
  print(x, end = " ")
else:
  print("\nFinally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement
for x in range(6):
  if x == 3: break
  print(x, end = " ")
else:
  print("\nFinally finished!")
print()

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
# for loops cannot be empty, but if we for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass