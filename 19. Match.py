"""
Instead of writing many if..else statements, we can use the match statement.

The match statement selects one of many code blocks to be executed.

Syntex
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

"""
# Simple match example
day = 5
match day:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thrusday")
    case 7:
        print("Friday")

# Default Value
day = 4
match day:
    case 6 :
        print("This is Thrusday. Our weekend")
    case 7 :
        print("This is Friday. This is also weekend")
    case _:
        print("Looking forward to the Weekend")

# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("No Weekend..!")
    case 6 | 7:
        print("Today is the weekend")

# If Statements as Guards
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("It's April and not weekend")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("It's May and not weekend")
    case _:
        print("No Mathch")
