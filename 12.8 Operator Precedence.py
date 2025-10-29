"""
1. Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
2. Exponentiation operator (**) comes next
3. Multiplication (*), Division (/), Floor Division (//), and Modulus (%) have the same precedence and are evaluated from left to right
4. Addition (+) and Subtraction (-) have the same precedence and are evaluated from left to right
5. Comparison operators (==, !=, >, <, >=, <=) are evaluated next
6. Bitwise operators (&, |, ^, ~, <<, >>) are evaluated after comparison operators
7. Logical operators (and, or, not) have the lowest precedence and are evaluated last

"""

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(2 ** 3 * 3 / 4 // 2 + 5 - 6)
print(3 + 5 > 2 + 8)