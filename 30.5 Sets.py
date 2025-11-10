import re
### [arn]	Returns a match where one of the specified characters e.g (a, r, or n) is present

txt = "The rain in Spain"

# Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)

y = re.findall("[nmS]", txt)    # So inside the [] we can find any character
print(y)
print()



### [a-n]	Returns a match for any lower case character, alphabetically between e.g (a and n)
txt = "The rain in Spain"

x = re.findall("[a-z]",txt)
y = re.findall("[A-Z]",txt)
print(x)
print(y)
print()



### [^arn]	Returns a match for any character EXCEPT e.g (a, r, and n)
x = re.findall("[^arn]",txt)
print(x)



### [0123]	Returns a match where any of the specified digits e.g (0, 1, 2, or 3) are present
text = "This is Number 31. This is another number 100"
x = re.findall("[123]",text)
print(x)
print()



### [0-9]	Returns a match for any digit between 0 and 9
x = re.findall("[0-5]",text)
print(x)
print()




### [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
txt = "8 times before 11:45 AM"
txt1 = "He have 100 balls and 150 marbles"

x = re.findall("[2-5][4-5]",txt)    # possible number for this are -> 24, 25, 34, 35, 44, 45, 54, 55
y = re.findall("[0-5][5-9][0-1]",txt1)
# here, first [] says the first number is in between 0 to 5
# second number is in between 5 to 9
# third number is in between 0 to 1
print(x)
print(y)
print()



### [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)

print(x)
print()



### [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
txt = "8 times before 11:45 AM"

#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)

txt = "I child can say 1 + 1 is equal to 2"
x = re.findall("[+]",txt)
print(x)