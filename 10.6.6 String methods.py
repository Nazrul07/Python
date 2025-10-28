## Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)


## 	Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "Welcome to my 2nd world"
x = txt.title()
print(x)

# -> first letter after a non-alphabet letter is converted into a upper case letter
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)


## Returns a translated string

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# -> Use a mapping table to replace many characters
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))


## Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()
print(x)


## 	Fills the string with a specified number of 0 values at the beginning
txt = "10"
x = txt.zfill(5) # Total will be 5 character(include the given text)
print(x)