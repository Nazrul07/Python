"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""
## If conditions

a = 33
b = 200
if b > a:
  print("b is greater than a\n")

number = 15
if number > 0:
  print("The number is positive\n")

"""
If statement, without indentation
if b > a:
print("b is greater than a") # will get an error

"""

## Multiple Statements in If Block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights\n")

## Using a boolean variable
is_logged_in = True
if is_logged_in:
  print("Welcome back!\n")

"""
Note:
Python can evaluate many types of values as True or False in an if statement.

Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.

This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).

"""



### Else if condition -> Elif
"""
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

"""

a = 33
b = 33
if b > a:
  print("b is greater than a\n")
elif a > b:
  print("a is greater than b\n")
elif a == b:
  print("a and b are equal\n")

# Multiple Elif Statements
score = 70

if score >= 80:
  print("Grade: A+\n")
elif score >= 75:
  print("Grade: A\n")
elif score >= 70:
  print("Grade: A-\n")
elif score >= 65:
  print("Grade: B+\n")

"""
-> When we use elif, Python evaluates the conditions from top to bottom.
-> As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
-> Only the first true condition will be executed.
-> Even if multiple conditions are true, Python stops after executing the first matching block.

"""

# Use elif when we have multiple mutually exclusive conditions to check.
# This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.
day = 3

if day == 1:
  print("Monday\n")
elif day == 2:
  print("Tuesday\n")
elif day == 3:
  print("Wednesday\n")
elif day == 4:
  print("Thursday\n")
elif day == 5:
  print("Friday\n")
elif day == 6:
  print("Saturday\n")
elif day == 7:
  print("Sunday\n")



## Else Statement
"""
The else keyword catches anything which isn't caught by the preceding conditions.

The else statement is executed when the if condition (and any elif conditions) evaluate to False.

"""
a = 200
b = 33
if b > a:
  print("b is greater than a\n")
elif a == b:
  print("a and b are equal\n")
else:
  print("a is greater than b\n")


number = 7
if number % 2 == 0:
  print("The number is even\n")
else:
  print("The number is odd\n")


username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")