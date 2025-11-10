"""
*****Regular Expression*****

-> is a sequence of characters that forms a search pattern.
-> RegEx can be used to check if a string contains the specified search pattern.
-> A search pattern is a rule or template that describes what kind of text we want to find in a string.

"""

## RegEx Module
import re

txt = "The rain in the Spain"
x = re.search("^The.*Spain$",txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
print()


"""
^ (Caret): This anchor asserts a match only at the start of the string.
$ (Dollar sign): This anchor asserts a match only at the end of the string.

"""

# Finding at any position of the string
txt = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. The rain in the Spain. Officiis nulla amet quibusdam recusandae doloribus qui."

x = re.search("The.*Spain",txt)         # " -> means staring of the search string and * -> means ending of the search string
if x:
  print("Yes! We have a match")
  print(x)
  print(f"Match found: {x.group}")      # This tells the interpreter: "Give me a reference to the thing named group that is attached to the object x."
  # Since "group" is a function (or method) that belongs to the re.Match object, Python returns a description of that function/method, including its type (built-in method) and its location in memory (at 0x...).

  print(f"Match found: {x.group()}")    # The group() method is designed to compute and return the actual string that matched the regular expression.
else:
  print("No Match")
print()

print(x.start())                        # Returns the starting index of the match.
print(x.end())                          # Returns the index just after the end of the match.
print(x.span())                         # Returns a tuple containing the start and end indices (start, end).