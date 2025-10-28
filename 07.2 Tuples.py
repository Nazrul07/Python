"""
Why tuple while we have list?

-> The performance of tuple is faster than list
-> Tuple is hashable
-> works with fixed data

"""

my_tuple = ("Nazrul", 24, 3.68, True)
print(my_tuple)
print("My name: ", my_tuple[0])
print()

# nested tuple -> 2D tuple
nested = ("a", "b", ("x", "y"))
print(nested)
print(nested[0][0])
print(nested[1][0])
print(nested[2][1])
# print(nested[2][2]) # Wrong -> sized exceeded
print()

new_tuple = ("Hello World..!", "Welcome to Python", "3.13", 11)
print(new_tuple)
'''
Wrong

new_tuple[2] = 3 # Can't change tuple element
print(new_tuple[2])

'''
