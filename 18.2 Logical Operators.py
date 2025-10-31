"""
Logical operators are used to combine conditional statements. Python has three logical operators:

and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true

"""

a = 200
b = 33
c = 500
# AND Operator
if a > b and c > a: # Both condition need to be true to execute the if statement
  print("Both conditions are True")

# OR Operator
if a > b or a > c: # Just one condition need to be true to execute
  print("At least one of the conditions is True")

# not Operator
if not b > c:
  print("b is NOT greater than c")


# Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# Using parentheses for complex conditions
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
print()


username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")


score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")