thistuple = ("apple", "banana", "cherry")

# Loop Through a Tuple
for i, x in enumerate(thistuple):
  print(x, end=" " if i != len(thistuple) - 1 else "\n")

# Loop Through the Index Numbers
for i in range(len(thistuple)):
  print(thistuple[i], end=" " if i != len(thistuple) - 1 else "\n")

# Using a While Loop
i = 0
while i < len(thistuple):
  print(thistuple[i], end=" " if i != len(thistuple) - 1 else "\n")
  i = i + 1