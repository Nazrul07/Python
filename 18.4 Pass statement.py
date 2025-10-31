# if statements cannot be empty, but if we for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass # No output


"""
Why Use pass?
The pass statement is useful in several situations:

When we're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that we plan to implement later

"""

score = 85

if score > 90:
  pass # This is excellent
print("Score processed")



value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")



check = True
if check:
  pass # Print nothing
else:
  print("Check again")