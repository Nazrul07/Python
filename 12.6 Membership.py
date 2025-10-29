"""
in  	-> Returns True if a sequence with the specified value is present in the object

not in 	-> Returns True if a sequence with the specified value is not present in the object

"""

fruit = ["apple", "banana", "cherry"]
print("banana" in fruit)    
print("pineapple" not in fruit)
print()

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)
print(" " in text)