# If we have only one statement to execute, we can put it on the same line as the if statement.
a = 10
if a > 5 : print("YES\n")

# Short Hand If ... Else
A = 2
B = 5
print("A") if A > B else print("B")
print()


# Assign a Value With If ... Else
a = 10
b = 20
bigger = a if a > b else b
print(bigger)

# Multiple Conditions on One Line
a = 2
b = 5
c = 2
print("a") if a > b and a > c else print("b") if b > c else print("c")
print()
# While one-liners look fancy, they can become hard to read if there are more than 2–3 conditions.
# For clarity, it’s better to use the normal if-elif-else structure for longer logic.

"""
When to use Shorthand If?

-> The condition and actions are simple
-> It improves code readability
-> We want to make a quick assignment based on a condition

"""

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)