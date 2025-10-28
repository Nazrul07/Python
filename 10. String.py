print('Hello'); print("Hello")

# Multiline string
a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# string index
print(a)
print(a[10])

# looping
for x in "Nazrul Islam":
  print(x, end = "")
print()

# string lenght
print(len(a))
print()

# ***** finding in string *****
txt = "The best things in life are free!"
print("life" in txt)

# using if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print()

txt = "The best things in life are free!"
print("expensive" not in txt)