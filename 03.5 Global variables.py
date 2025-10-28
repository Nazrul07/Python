x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
print()

#But
def myfunc():
  x = "fantastic"
  print("Python is " + x) # Under funtion local > global

myfunc()
print("Outsider the function: ", x)
print()


def myfunc1():
  global x          # Will be updated
  x = "fantastic"

def myfunc2():
  x = "easy"        # Change localy only
  print("Inside function --> Python is " + x)

myfunc1()
print("Python is " + x)

myfunc2()
print("Outsize function --> Python is " + x)