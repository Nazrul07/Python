# *****Positional-Only Arguments*****
# Normally
def my_function(name):
    print("Hello", name)

my_function("Emil")          # ✅ positional
my_function(name="Emil")     # ✅ keyword

# Positional-only
def my_function(name, /):    # Everything before / must be passed by position, not by keyword.
    print("Hello", name)

my_function("Emil")          # ✅ works
# my_function(name="Emil")   # ❌ TypeError


def greet(first, last, /, title="Mr."):
    print(f"Hello {title} {first} {last}")

greet("John", "Doe")                   # ✅ ok
greet("John", "Doe", title="Dr.")      # ✅ ok
# greet(first="John", last="Doe")      # ❌ Error
print()

# *****Keyword-Only Arguments*****
# To specify that a function can have only keyword arguments, add *, before the arguments

def my_function(*, name):
    print("Hello", name)
my_function(name = "Nazrul")

# With * , we will get an error if we try to use positional arguments
"""
Error:
def my_function(*, name):
  print("Hello", name)

my_function("Emil")

"""


# *****Combining Positional-Only and Keyword-Only*****
def my_function(a, b, /, *, c, d): # Means a and b must be Positional-Only and c and d must be Keyward-Only
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)