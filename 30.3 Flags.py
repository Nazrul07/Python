# We can add flags to the pattern when using regular expressions
import re
"""
re.ASCII	re.A	Returns only ASCII matches

"""

txt = "Åland10"

#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))

#Without the flag, the example would return all character:
print(re.findall("\w", txt))

#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A), "\n")


"""
re.DEBUG		Returns debug information

"""
txt = "The rain in Spain"

#Use a case-insensitive search when finding a match for Spain in the text:

print(re.findall("spain", txt, re.DEBUG),"\n")

# This section shows that the engine is compiling our pattern into a sequence of literal characters to match,
# using their ASCII (or Unicode) decimal values

# LITERAL 115   -> s
# LITERAL 112   -> p
# LITERAL 97    -> a
# LITERAL 105   -> i
# LITERAL 110   -> n



# The INFO block describes how the engine optimizes the search using algorithms
# like the Boyer-Moore or Rabin-Karp to quickly scan the string.

# 0. INFO 16 0b11 5 5 (to 17)
#       prefix_skip 5
#       prefix [0x73, 0x70, 0x61, 0x69, 0x6e] ('spain')
#       overlap [0, 0, 0, 0, 0]
# 17: LITERAL 0x73 ('s')
# ...
# 27. SUCCESS
# The debug output essentially tells us: "I am looking for the exact, literal, case-sensitive sequence 'spain'."



"""
re.DOTALL	re.S	Makes the . character match all characters (including newline character)

"""

txt = """Hi
my
name
is
Nazrul"""

#Search for a sequence that starts with "me", followed by one character, even a newline character, and continues with "is":
print(re.findall("me.is", txt, re.DOTALL))

#This example would return no match without the re.DOTALL flag also:
print(re.findall("ul.", txt, re.DOTALL))    # There is nothing after the "ul"

#Same result with the shorthand re.S flag:
print(re.findall("me.is", txt, re.S),"\n")



"""
re.IGNORECASE	re.I	Case-insensitive matching

"""
txt = "The rain in Spain"
target = "spain"

#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall(target, txt, re.IGNORECASE))

#Same result using the shorthand re.I flag:
print(re.findall(target, txt, re.I), "\n")



"""
re.MULTILINE	re.M	Returns only matches at the beginning of each line

"""
txt = """There
aint much
rain in 
Spain.

There
aint much
rain in 
Spain"""

#Search for the sequence "ain", at the beginning of a line:
print(re.findall("^ain", txt, re.MULTILINE))    # at start only
print(re.findall("ain", txt, re.MULTILINE))     # anywhere of the string

#This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning of the text:
print(re.findall("^ain", txt))

#Same result with the shorthand re.M flag:
print(re.findall("^ain", txt, re.M))


"""
re.NOFLAG		Specifies that no flag is set for this pattern
"""


"""
re.UNICODE	re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches

Pattern         Meaning with re.UNICODE
\w              Matches letters from any language, digits, and the underscore. (e.g., Å, é, ç, $\beta$)
\d              Matches any character that is considered a digit in Unicode (e.g., Arabic-Indic digits, not just 0-9)
\s              Matches any Unicode whitespace character (e.g., non-breaking space, thin space, etc.).

"""

txt = "Åland"

#Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE))

#Same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U))



"""
re.VERBOSE	re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable.

"""
text = "The rain in Spain falls mainly on the plain. ain"

#Find and return words that contains the phrase "ain":

pattern = """
[A-Za-z]* # starts with any letter or nothing
ain+      # must contains 'ain'
[a-z]*    # followed by any small letter or not
"""
print(pattern)
print(re.findall(pattern, text, re.VERBOSE))

#The example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, text))

#Same result with the shorthand re.X flag:
print(re.findall(pattern, text, re.X))


txt = "This is number 30. This is another number 70. 70 is greater than 30. They both divisiable by 2, 5, 10"
pattern = """
[A-Za-z]*   # starts with any letter or nothing
an          # must contains 'an'
[a-z]*      # followrd by any small latter or not
"""
print(re.findall(pattern, txt, re.VERBOSE))