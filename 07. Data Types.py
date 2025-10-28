# string
x1 = "Hello World"
print(type(x1))

# integer
x2 = 20
print(type(x2))

# float
x3 = 20.05
print(type(x3))

# complex number
x4 = 1j
print(type(x4))

# list -> it can update, delete or modify
x5 = ["apple", "berry", "banana"]
print(type(x5))

# Tuple - > Have fixed position. Cannot change, add, or remove items after creation. Allows duplicates.
x6 = ("apple", "banana", "cherry")
print(type(x6))

# Range
x7 = range(6)
print(type(x7))

# Dict
x8 = {"name": "Nazrul", "age": 24}
print(type(x8))

# frozenset
x9 = frozenset({"apple", "banana", "orange"})
print(type(x9))

# bool
x10 = True
print(type(x10))

# bytes
x11 = b"Hello"
print(type(x11))

# bytearray
x12 = bytearray(5)
print(type(x12))

# MemeoryView
x13 = memoryview(bytes(5))
print(type(x13))

# NoneType
x14 = None
print(type(x14))
