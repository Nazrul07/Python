# Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# Returns a left trim version of the string
# -> by default it trims space from left size
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)


# Returns a right trim version of the string
# -> by default it trims space from right side
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.rstrip(",.asw")
print(x)

# Returns a both side trim version of the string
# -> by default it trims space from both sides
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana,,,.....ssssswwwwa"
x = txt.strip(",.asw")
print(x)


# Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hello World!"
mytable = str.maketrans("World", "Earth") # size should be same. Otherwise, will not work.
"""
W → E
o → a
r → r
l → t
d → h
"""
# print(mytable)
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable1 = str.maketrans(x, y)
print(txt.translate(mytable1))


txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
"""
x → characters to replace
y → characters to replace them with
z → characters to delete
"""
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

# Returns a tuple where the string is parted into three parts
# -> This method searches for a specified string, and splits the string into a tuple containing three elements.
txt = "I could eat bananas all day"
x = txt.partition("apples") # If the specified value is not found. the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string
print(x)

x = txt.partition("bananas")
print(x)

# Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "watermelon")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2) # Replace the two first occurrence of the word "one"
print(x)