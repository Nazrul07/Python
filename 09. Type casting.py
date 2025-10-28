a = 5
b = 2.54
c = 1 + 2j
d = "Hello"

print(a, end = " ")
print(float(a), end = " ")
print(str(a), end = " ")
print(complex(a))

print(b, end = " ")
print(int(b), end = " ")
print(str(b), end = " ")
print(complex(b))

print("Original:", c, end = " ")
print("Real Part:", c.real, end = " ")
print("Complex Part:", c.imag, end = " ")
print("Absolute value:",abs(c))

print(d, end = " ")
