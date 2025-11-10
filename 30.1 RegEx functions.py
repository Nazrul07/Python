# The re module offers a set of functions that allows us to search a string for a match

import re

"""
***** The findall() function*****

is designed to return a list of the matched strings (or captured groups),
but it does not return the position (index) of those matches.

"""
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# But we can find the position in a different way at which they are in
txt = "The rain in Spain"
pattern = "ai"

matches = re.finditer(pattern, txt)
# print(matches)
for match in matches:
    print(f"Match: '{match.group()}' found at position: {match.span()}")



"""
*****The search() Function*****

The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

"""

x = re.search("\s", txt)        # \s means - > Returns a match where the string contains a white space character

print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned



"""
*****The split() Function*****

The split() function returns a list where the string has been split at each match

"""
x = re.split("\s", txt)     # Split at each white-space character
print(x)

# We can control the number of occurrences by specifying the maxsplit parameter
# Split the string only at the first occurrence
x = re.split("\s", txt, 1)  # Max -> 1 split
print(x)
print()



"""
*****The sub() Function*****
The sub() function replaces the matches with the text of our choice

"""
x = re.sub("\s", "9", txt)  # Replace every white-space character with the number 9
print(x)

# We can control the number of replacements by specifying the count parameter
x = re.sub("\s", "9", txt, 2)   # for two times only
print(x)