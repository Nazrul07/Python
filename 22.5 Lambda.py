# Python Lambda

"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntex:
lambda arguments : expression

"""
x = lambda a : a + 10
print(x(5))

# Lambda functions can take any number of arguments
x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b * c
print(x(5, 6, 2))
print()


"""
Why Use Lambda Functions?

The power of lambda is better shown when we use them as an anonymous function inside another function.
We have a function definition that takes one argument, and that argument will be multiplied with an unknown number

"""

def myfun(n):
    return lambda a : a * n

mydoubler = myfun(2)
mytripler = myfun(3)
print(mydoubler(11))
print(mytripler(10))

# Use lambda functions when an anonymous function is required for a short period of time.



## Lambda with Built-in Functions
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# The map() function applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 3, numbers)) # The map() function applies a function to every item in an iterable
# map() doesn’t immediately return a list — it returns a map object (iterator).
# To see the actual results, we must convert it to a list
print(doubled)



## Using Lambda with filter()
# The filter() function creates a list of items for which a function returns True
number = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x : x % 2 == 0, number))
print(even)


## Using Lambda with sorted()
# The sorted() function can use a lambda as a key for custom sorting.

# Sort a list of tuples by the second elemen
students = [("Hasna", 3.78), ("Provat", 3.81), ("Yasir", 3.499), ("Nazrul", 3.681), ("Sayem", 3.2)]
sorted_by_cgpa = sorted(students, key = lambda x: x[1])
print(sorted_by_cgpa)


# Sort strings by length
fruits = ["Apple", "Banana", "Orange", "Pepe", "Guava", "Lichi"]
updating = sorted(fruits, key = lambda x : len(x))
print(updating)