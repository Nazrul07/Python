## Searches the string for a specified value and returns the last position of where it was found
# -> method returns -1 if the value is not found.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10) # only search between position 5 and 10
print(x)

if(txt.rfind("z") == -1):
    print("No found")

# -> rfind and rindex almost similar just one difference is:

text = "Hello world"
print(text.rfind("python"))   # → -1
# print(text.rindex("python"))  # → ValueError: substring not found
# -> for which rfind is more safer becasue it does not create error


## Returns a right justified version of the string
txt = "banana"
x = txt.rjust(20) # -> left align
print(x, "is my favorite fruit.")

x = txt.rjust(20, "_") # replace with _
print(x)


## Search for the last occurrence of the word and return a tuple with three element
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
print(x[0], x[1], x[2])


## 	Splits the string at the specified separator from backward, and returns a list
txt = "apple, banana, cherry, orange"
x = txt.rsplit(", ")
print(x)
print(x[0], x[1], x[2], x[3])

txt = "apple, banana, cherry, orange"
# setting the maxsplit parameter to 2, will return a list with 3 elements!
x = txt.rsplit(", ", 2)
print(x)
print(x[0], x[1], x[2])


## 	Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = ",,sswws...banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw") # -> Remove the trailing characters if they are commas, periods, s, q, or w
print(x)

## Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
print("List:",x)
print("Lenght:",len(x))

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ") # -> Split the string, using comma, followed by a space, as a separator:
print(x)


## Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines() # by default it does not keep the line break
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True) # keep the line break
print(x)


## Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20) # -> Check if position 7 to 20 starts with the characters "wel"
print(x)

txt = "Hi, welcome to my world."
x = txt.startswith(("Hello", "Hi", "Greeting")) # -> Check if the string starts with either "Hello" or "Hi"
print(x)

## Returns a trimmed version of the string

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)