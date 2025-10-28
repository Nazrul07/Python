'''
-> Cannot change it after it's created but it is hashable whereas set is not.
'''

x = frozenset({"apple", "banana", "cherry"})
print(x)


x = frozenset(["apple", "banana", "cherry"])
y = frozenset(["banana", "mango"])

# set operations still work!
print(x.union(y))        # combine
print(x.intersection(y)) # common items
print(x.difference(y))   # unique items in x
print()

fset = frozenset(["python", "java"])
data = {fset: "Programming Languages"}
print(data)
