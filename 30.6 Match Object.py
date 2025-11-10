import re
### A Match Object is an object containing information about the search and the result.

txt = "The rain in Spain"
x = re.search("ai", txt)
print(type(x))
print(x) #this will print an object
print()

## The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() -> returns a tuple containing the start-, and end positions of the match.
# .string -> returns the string passed into the function
# .group() -> returns the part of the string where there was a match

text = "Sun shines over the Sky and Stars sparkle at night."
pattern = r"\bS\w+"     # Find the word start with S
x = re.search(pattern, text)       # Return the object when it finds the match
print(x)
print(x.start())        # Return the starting position where we found the first match
print(x.end())          # Return the ending position where we found the first match
print(x.span())         # Return the position where .search found the first match
print(x.string)         # Return the string on which we are working on
print(x.group())        # Part of the string where we found the match

# If there is no match, the value None will be returned, instead of the Match Object.