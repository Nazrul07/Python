# Example 1
x = 74

if x >= 40:
    if x >= 50:
        if x >= 60:
            if x >= 70:
                if x>= 80:
                    print("A+")
                else:
                    print("A")
            else:
                print("A-")
        else:
            print("B")
    else:
        print("C")
else:
    print("F")


# Example 2
age = 25
has_license = False

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


# Example 3
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")