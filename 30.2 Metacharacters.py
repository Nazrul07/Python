import re

txt = "The rain in Spain"

"""
[]	-> A set of characters	"[a-m]"

"""

x = re.findall("[a-m]", txt)    # return a list
print(x)

x = re.findall("[A-Z]", txt) 
print(x)

data_string = "Order: 45, Quantity: 200, Total: 12.50"
x_digits = re.findall("[0-9]", data_string)
print(x_digits)


"""
\	-> Signals a special sequence (can also be used to escape special characters)

"""

txt = "That will be 59 dollars"

#Find all digit characters: \d

x = re.findall("\d", txt)
print(x)



"""
.	-> Any character (except newline character)

"""
txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)


txt1 = "Hello, How it's going?"
x = re.findall("go...", txt1)
y = re.findall("i...", txt1)
z = re.findall("i..s", txt1)
print(x)
print(y)
print(z)
print()


"""
^   -> Starts with

"""
txt = "Hello planet"
x = re.findall("^Hello",txt)
if x:
  print("Yes, the string starts with 'Hello'")
else:
  print("No match")
print(x, "\n")


"""
$	-> Ends with

"""
txt = "hello planet"
x = re.findall("planet$",txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
print(x, "\n")



"""
*	-> Zero or more occurrences

"""
txt = "hello planet"
txt1 = "This is new World"
x = re.findall("he.*o",txt)
y = re.findall("T.*s", txt1)     # Trying to find 'This is'
z = re.findall("W.*d",txt1)
p = re.findall("i.*s",txt1)
print(x)
print(y)
print(z)
print(p,"\n")



"""
+	-> One or more occurrences

"""
txt = "hello planet"
x = re.findall("h.+", txt)
y = re.findall("h.+o",txt)
print(x)
print(y,"\n")



"""
?	-> Zero or one occurrences

"""
txt = "hello planet"
x = re.findall("l.?",txt)
y = re.findall("o.?",txt)
z = re.findall("he.?o",txt)
p = re.findall("hel.?o",txt)
print(x)
print(y)
print(z)
print(p, "\n")



"""
{}	-> Exactly the specified number of occurrences

"""
txt = "hello planet"
x = re.findall("he.{2}o",txt)
y = re.findall("h.{3}o",txt)
z = re.findall("h.{2}o",txt)
print(x)
print(y)
print(z, "\n")



"""
|   -> Either or

"""
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|plain|rain", txt)  # checking either it's containing falls or stays in the string. Answer can be multiple not only one
y = re.findall("spain|new", txt)

print(x)
print(y)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
