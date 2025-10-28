# ***** Capitalization *****
txt = "hello, world"
print(txt.capitalize()) # Converts the first character to upper case

# ***** To lower *****
txt = "Hello, World"
print(txt.casefold())  # Make the string lower case
txt = "Hello, World"
print(txt.lower()) 

# ***** Allign -> center align the string ******
txt = "banana"
x = txt.center(20)
print(x)

# ****** Count *****
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# Search from position 10 to 24
x = txt.count("apple", 10, 24)
print(x)

# ****** encode *****
txt = "My name is Nazrul"
x = txt.encode()
print(x)

# ***** endswith ***** 
txt = "Hello, welcome to my world"
x = txt.endswith("world") # Check if the string ends with
print(x)

# Search from position 5 to 11
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

# ***** Expandtabs *****
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# ***** Finding *****
txt = "Hello, welcome to my world."
x = txt.find("welcome") # Return the position
print(x)

x = txt.find("e", 5, 10) # Search in position
print(x)
print(txt.index("welcome")) # Although both find and index gives the index value

# ***** Formating ******
# .format just replace the current value with given new one
txt1 = "My name is {fname}, I'm {age}. ".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}. ".format("John",36)
txt3 = "My name is {}, I'm {}.".format("John",36)

print(txt1, txt2, txt3)

# left align (:<) -> after the point
txt4 = "We have {:<8} chickens.".format(49)
print(txt4)

# right align(:>) -> before the point
txt5 = "We have {:>8} chickens.".format(49)
print(txt5)

# center align -> both sides
txt6 = "We have {:^8} chickens.".format(49)
print(txt6)

# Places only the sign to the left most position and number to the right
txt7 = "The temperature is {:=8} degrees celsius.".format(-5)
print(txt7)

# Use a plus sign to indicate if the result is positive or negative
txt8 = "The temperature is between {:+} and {:+} degrees celsius.".format(-3, 7)
print(txt8)

# Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign)
txt9 = "The temperature is between {:-} and {:-} degrees celsius.".format(-3, 7)
print(txt9)

# Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers. Don't add extra space before negative number.
txt10 = "The temperature is between {: } and{: } degrees celsius."
print(txt10.format(-3, 7))

# Use "," to add a comma as a thousand separator
txt11 = "The universe is {:,} years old."
print(txt11.format(13800000000))

# Use "_" to add a underscore character as a thousand separator
txt12 = "The universe is {:_} years old."
print(txt12.format(13800000000))

# Use "b" to convert the number into binary format -> same number only
txt13 = "The binary version of {0} is {0:b}. This is another {0}."
print(txt13.format(5))

# Converts the value into the corresponding unicode character
txt14 = "The unicode of {0} is {0:c}."
print(txt14.format(38))

# Use "d" to convert a number, in this case a binary number, into decimal number format
txt15 = "We have {:d} chickens."
print(txt15.format(0b101)) # binary to decimal

print(txt15.format(0o12)) # octal to decimal

print(txt15.format(0xF)) # hexadicimal to decimal

# decimal to binary, octal, hexadecimal
num = 15
print("Binary: {:b}".format(num))
print("Octal: {:o}".format(num))
print("Hex: {:x}".format(num))

# Use "e" to convert a number into scientific number format (with a lower-case e)
txt16 = "The total value is about {:e} dollars."
print(txt16.format(19200))

# Use "E" to convert a number into scientific number format (with a upper-case E)
txt17 = "The total value is about {:E} dollars."
print(txt17.format(19200))

# Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals
txt18 = "The price is {:.2f} dollars."
print(txt18.format(45))

# without the ".2" inside the placeholder, this number will be displayed like this:
txt19 = "The price is {:f} dollars."
print(txt19.format(45))

# Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
# print(x)
txt20 = "The price is {:F} dollars."
print(txt20.format(x))

# same example, but with a lower case f:
txt21 = "The price is {:f} dollars."
print(txt21.format(x))

# General format
txt22 = "The price is {:g} dollars."
print(txt22.format(10.2))

txt23 = "The price is {:G} dollars." # capital G for upper format
print(txt23.format(123456789.0))

txt24 = "The price is {:g} dollars."
print(txt24.format(0.00001234))

# Use "%" to convert the number into a percentage format
txt = "You scored {:%}"
print(txt.format(0.25446))

#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.255))
