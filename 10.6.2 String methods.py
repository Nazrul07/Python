# Alphanumeric -> Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12" # " "(space) is not alphanumeric 
x = txt.isalnum()
print(x)

# Alphabet -> Returns True if all characters in the string are in the alphabet
txt = "Company"
x = txt.isalpha()
print(x)

txt = "Company4"
x = txt.isalpha()
print(x)

# ASCII -> Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print(x)

# Returns True if all characters in the string are decimals
txt = "192"
print(txt.isdecimal())

txt1 = "Hello"
print(txt1.isdecimal())

# Returns True if all characters in the string are digits
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())

# Returns True if the string is an identifier
"""
A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
A valid identifier cannot start with a number, or contain any spaces.
"""

txt = "Demo"
x = txt.isidentifier()
print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())