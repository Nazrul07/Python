import re

### /A    -> Returns a match if the specified characters are at the beginning of the string

txt = "The rain in Spain"

# Check if the string starts with "The":

x = re.findall(r"\AThe", txt)   # We need to use extra r before the operation. Because in Python, the backslash (\) is an escape character. The "r" in the beginning is making sure that the string is being treated as a "raw string"

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
print()




### \b	-> Returns a match where the specified characters are at the beginning or at the end of a word

txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
y = re.findall(r"\bTh", txt)    #Check if "Th" is present at the beginning of a WORD
z = re.findall(r"ain\b",txt)    # Check if "ain" is present at the end of a WORD
print(x)
print(y)
print(z, "\n")



### \B	-> Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
txt = "The rain in Spain"

# Check if "The" is present, but NOT at the beginning of a word:
x = re.findall(r"\BThe", txt)
print(x)

#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)



### \d	-> Returns a match where the string contains digits (numbers from 0-9)
txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):
x = re.findall(r"\d", txt)
print(x)

if x:
  print("Digit available")
else:
  print("Contains no digit")



### \D	-> Returns a match where the string DOES NOT contain digits.

txt = "This is number 31"
#Return a match at every no-digit character:
x = re.findall(r"\D", txt)

print(x)
print()



### \s	-> Returns a match where the string contains a white space character
txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall(r"\s", txt)

print(x)
print()


### \S	-> Returns a match where the string DOES NOT contain a white space character
txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall(r"\S", txt)

print(x)
print()


### \w	-> Returns a match where the string contains any word characters
txt = "The rain in Spain_ 100"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall(r"\w", txt)

print(x)
print()


### \W	-> Returns a match where the string DOES NOT contain any word characters
txt = "The rain in Spain_ 100 ?*&"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)

print(x)
print()



### \Z	-> Returns a match if the specified characters are at the end of the string
txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)

print(x)