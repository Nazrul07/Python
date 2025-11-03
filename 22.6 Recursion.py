"""
*****Recursion*****

-> Recursion is when a function calls itself.
-> Recursion is a common mathematical and programming concept.
It means that a function calls itself. 
This has the benefit of meaning that we can loop through data to reach a result.
-> The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates,
or one that uses excess amounts of memory or processor power.
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

"""

# Printing 1 to 10
def rec(n):
    if(n == 0):
        return
    rec(n-1)
    print(n)

rec(10)
print()


# Countdown 
def rec(n):
    print(n)
    if(n == 1):
        return
    rec(n-1)

rec(5)
print()


# Another way

def rec(n):
    if n <= 1: pass

    else:
        rec(n-1)
    print(n)
    
rec(10)
print()


def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(10)
print()



## Factorial
def factorial(n):
   if n == 1:
      return 1
   else:
      return n * factorial(n-1)
   
print(factorial(5))
print()




## Fibonacci Sequence -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34....
# -> start from 0th position
def fibo(n):
   if(n <= 1):
      return n
   else:
      return fibo(n-1) + fibo(n-2)
print(fibo(6))




## Sum of a list using recursion
def sum_num(n):
   if len(n) == 0:
      return 0
   else:
      return n[0] + sum_num(n[1:])

num = [1, 2, 3, 4, 5]
print(sum_num(num))
print()

"""
When the list has 1 element, e.g. [5] —
then numbers[0] is 5, but what about numbers[1:]?

-> When we slice a list in Python — it never raises an IndexError.
numbers = [5]
print(numbers[1:])   # []

So numbers[1:] gives us an empty list, not an error.

When the list has one element-
Accessing numbers[1] → would cause IndexError
But slicing numbers[1:] → returns an empty list ([])

"""



## Maximum value from a list
def find_max(nums):
   if len(nums) == 1:
      return nums[0]
   else:
      max_of_rest = find_max(nums[1:])
      return nums[0] if nums[0] > max_of_rest else max_of_rest
   
"""
# More easier function
def find_max(nums):
    return nums[0] if len(nums) == 1 else max(nums[0], find_max(nums[1:]))

"""

number_list = [10, 20, 11, 25, 30, 22, 29]
print(find_max( number_list))
print()



## Recursion Depth Limit
# Python has a limit on how deep recursion can go.
# The default limit is usually around 1000 recursive calls.

# Checking the recursion limit
import sys
print(sys.getrecursionlimit())

# We can increate the limit by doing:
sys.setrecursionlimit(2000) # Now it's 2000.
print(sys.getrecursionlimit())
# We can set the limit manually.But over 50,000 ⚠️ Very risky — may crash Python