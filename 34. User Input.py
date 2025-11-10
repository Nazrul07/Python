def welcome(name):
    print("Welcome " + name)

print("Enter you name:")
name = input()
welcome(name)

# Python stops executing when it comes to the input() function, and continues when the user has given some input.



## Using prompt
# In the example above, the user had to input their name on a new line.
# The Python input() function has a prompt parameter,
# which acts as a message we can put in front of the user input, on the same line:

name = input("Enter your name: ")
print(f"Hello {name}")



### Multiple Inputs
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")



### Input Number
# The input from the user is treated as a string. Even if, in the example above, We can input a number,
# the Python interpreter will still treat it as a string.
import math

x = input("Enter a number:")
print(type(x))
#find the square root of the number:
y = math.sqrt(float(x))     # We need to covert the string to number first
print(f"The square root of {x} is {y}")



### Validate Input
# It is a good practice to validate any input from the user.
# In the example above, an error will occur if the user inputs something other than a number.

# To avoid getting an error, we can test the input, and if it is not a number,
# the user could get a message like "Wrong input, please try again", and allowed to make a new input:

# Example
# Keep asking until you get a number:
y = True
while y is True:
    x = input("Enter a number: ")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong Input, please try again")

print("Thank You...!")