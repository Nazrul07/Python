# The try block lets us test a block of code for errors.

# The except block lets us handle the error.

# The else block lets us execute code when there is no error.

# The finally block lets us execute code, regardless of the result of the try- and except blocks.




### Exception Handling

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

try:
    print(x)    # Here I didn't initialize the x and tryping to printing the x. It's an error. So, instead of generating an error the except block will be executed.
except:
    print("An error occured")



## Many Exceptions
# We can define as many exception blocks as we want, e.g. if we want to execute a special block of code for a special kind of error:
try:
    print(x)
except NameError:
    print("Variable x is not defined before printing it.")
except:
    print("Something else went wrong...!")
print()


## Else
# WE can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello World")            # This will execute
except:
    print("An error occured. Go check again.")
else:
    print("Nothing went wrong.")    # There is no error. So, this will also be executed.
print()


## Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except NameError:
    print("Define the varibale x before printing it.")
except:
    print("Someting else went wrong..!")
else:
    print("No error raised.")
finally:
    print("We larned something...!")
print()


try:
    print("Hello there.")
except NameError:
    print("Define the varibale x before printing it.")
except:
    print("Someting else went wrong..!")
else:
    print("No error raised.")
finally:
    print("We larned something...!\n")


## Raise an exception

# As a Python developer we can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

"""
x = -1

if x < 0:
    raise Exception("Sorry, the number is below zero.")

"""

# raise = “throw an error intentionally.”
# Exception("message") = create a new error object.



# try-except handling - another example

def set_num(num):
    if num < 0:
        raise Exception("This number cannot be negative.")
    print("We can do our next operation.")

try:
    set_num(-2)
except Exception as e:
    print("Caught error:", e)



## ValueError

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age is set to {age}")

try:
    set_age(-2)
except ValueError as e:
    print("Caught error:", e)



## TypeError
def multi(data1, data2):
    if not (isinstance(data1, float) and isinstance(data2, float)):
        raise TypeError("Expected two floating point number. Got other datatypes expect floating point number.")
    print(data1 * data2)

try:
    # multi(10.2, 20)      # Error one is integer
    # multi(10.2, "new")   # Error one is string
    # multi(20.0, 10.5)     # Will work
    multi("Game", "Over")
except TypeError as e:
    print("Caught error:", e)