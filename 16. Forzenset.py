# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.

# Creating a frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

## Methods
# -> Returns a shallow copy
fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)
print()

# -> Returns a new frozenset with the difference
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
c = a.difference(b)
print(c)
print(a - b)
print()

# -> Returns a new frozenset with the intersection
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)
print()

# -> Returns whether two frozensets have an intersection
# -> Returns True if two sets have no common elements. If they share even one element, it returns False.
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))
print()

# -> Returns True if this frozenset is a (proper) subset of another
"""
Subset:   A ⊆ B      (A is inside B)
Superset: A ⊇ B      (A contains B)
Proper Subset: A ⊂ B  (A is inside B, and A ≠ B)
Proper Superset: A ⊃ B (A contains B, and A ≠ B)

"""
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))       # -> Checks whether all elements of a exist in b
print(a <= b)              # -> This is operator shorthand for issubset()
print(a < b)               # -> It returns True only if all elements of a are in b, and a ≠ b (they’re not equal).

# -> Returns True if this frozenset is a (proper) superset of another
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))     # Checks whether a contains all elements of b.
print(a >= b)              # It means “a is a superset of b”.
print(a > b)               # It returns True only if all elements of a are in b, and a ≠ b (they’re not equal).

# -> Returns a new frozenset with the symmetric differences
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)
print()

# -> Returns a new frozenset with the union of sets
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)
print()