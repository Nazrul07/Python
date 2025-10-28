"""
-> Range is efficient.
-> We use it for -> read iteams, Iterate, create new range
-> It's just like tuple.
-> Unlike a list, range doesn't store all numbers — it calculates them on the fly. This saves a lot of memory, especially for large sequences.

"""

x1 = range(5)
print(x1)
print(list(x1))
print()

x2 = range(2, 8)
print(x2)
print(list(x2))
print()

x3 = range(1, 10, 2) # range(start, end, step) where "step" means - difference between any consecutive two data
print(list(x3))
print()

x4 = range(1, 10, 3) 
print(list(x4))
print()

for i in range(10):
    print(i,end = " ")
print()

