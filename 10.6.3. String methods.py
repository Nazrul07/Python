# Returns True if all characters in the string are lower case

txt = "hello world!"
x = txt.islower()
print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


# Returns True if all characters in the string are numeric(0-9)
txt = "565543"
x = txt.isnumeric()
print(x)

# txt = 2
# print(txt.isnumeric()) # valid for string only


# Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "Hello!\nAre you #1?" # False, is beacuse \n escape character
x = txt.isprintable()
print(x)

# Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x)

txt = "   s   "
x = txt.isspace()
print(x)

# Returns True if the string follows the rules of a title
# -> Check if each word start with an upper case letter
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

a = "HELLO, AND WELCOME TO MY WORLD" # Not title
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())


# Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

# Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

myTuple = ("John", "Peter", "Vicky", "Arafat", "Hasan", "Nazrul", "Yasir")
x = ", ".join(myTuple)
print(x)

# Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

x = txt.ljust(20, "_")
print(x, "is my favorite fruit.")