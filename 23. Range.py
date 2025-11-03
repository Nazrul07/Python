"""
*****Python range*****

The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

This set of numbers has its own data type called range.
Immutable means that it cannot be modified after it is created.

"""
## One argument ---> Syntex: range(stop)
# The start argument is optional, and if not provided, it defaults to 0.
x = range(10) # Create a range of numbers from 0 to 9
print(x)

y = list(x)    # We can change the range into list or any iteratable
print(y, "\n")



## Two arguments     ---> Syntex: range(start, stop)
x = range(3, 9)
print(x)

y = list(x)
print(y, "\n")



## Three arguments    ---> Syntex: range(start, stop, step)
x = range(3, 10, 2) # ---> difference between two consecutive number in the range is the step.
print(x)
y = list(x)
print(y, "\n")



## Ranges are often used in for loops to iterate over a sequence of numbers.
for i in range(10):
  print(i, end = " ")
print()



## Using List to Display Ranges
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
print()



## Slicing Ranges
r = range(10)
print(r[2])
print(r[3:])
print()



## Membership Testing
r = range(0, 10, 2)
print(7 in r)
print(6 in r)
print(10 in r)
print()



## Length
r = range(0, 10, 2)
print(len(r))