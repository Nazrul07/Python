i, n = 1, 10

while i <= n:
  print(i, end = " " if i< n else "\n")
  i += 1

# With the break statement we can stop the loop even if the while condition is true
# i = 1, n = 10 # It will create error
"""
i = 1
n = 10
We can assign that way separately
or
"""
i = 1
while i <= n:
  print(i, end = " ")
  if i % 2 == 0 and i % 3 ==0 :
    break
  i += 1
print()

# With the continue statement we can stop the current iteration, and continue with the next
i = 1
while i <= n:
  if i % 2 == 0:
    i += 1
    continue
  print(i, end = " ")
  i += 1
print()

# The else Statement -> With the else statement we can run a block of code once when the condition no longer is true
i = 1
while i <= n:
  print(i, end = " " if i< n else "\n")
  i += 1
else:
  print("Loop statement is not ture")

  
  