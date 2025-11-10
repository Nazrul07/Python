### :<        -> Left aligns the result (within the available space)

# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
# Use "<" to left-align the value:

txt = f"We have {49:<8} chickens."
print(txt) 
print()



### :>      -> Right aligns the result (within the available space)

# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
# Use ">" to right-align the value:

txt = f"We have {10:>8} chickens."
print(txt)
print()



### :^		-> Center aligns the result (within the available space)

# To demonstrate, we insert the number 10 to set the available space for the value to 10 characters.
# Use "^" to center-align the value:

txt = f"We have {20:^10} chickens."
print(txt)
print()



### :=      -> Places the sign to the left most position

# To demonstrate, we insert the number 8 to specify the available space for the value.
# Use "=" to place the plus/minus sign at the left most position:

txt = f"The temperature is {-5:=8} degrees celsius."
print(txt)
txt1 = f"The temperature is {+10:=8} degrees celsius."
print(txt1)
print()



### :+      -> Use a plus sign to indicate if the result is positive or negative

# Use "+" to always indicate if the number is positive or negative:
txt = f"The temperature is between {-3:+} and {7:+} degrees celsius."
print(txt)



### :-      -> Use a minus sign for negative values only

# Use "-" to always indicate if the number is positive or negative:
txt = f"The temperature is between {-3:-} and {7:-} degrees celsius."
print(txt)


### :       -> Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)

# Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = f"The temperature is between {-3: } and {7: } degrees celsius."

print(txt)



### :,		-> Use a comma as a thousand separator

# Use "," to add a comma as a thousand separator:
txt = f"The universe is {13800000000:,} years old."

print(txt)



### :_		-> Use a underscore as a thousand separator
txt = f"The universe is {13800000000:_} years old."
print(txt)
print()



### :b		-> Binary format

a = 10
# Use "b" to convert the number into binary format:
txt = f"The binary version of {a} is {a:b}"
print(txt)



### :c		-> Converts the value into the corresponding Unicode character
a = 100
txt = f"The binary version of {a} is {a:c}"
print(txt)



### :d		-> Decimal format

# Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = f"We have {0b101:d} chickens."
print(txt)
txt1 = f"I have {0b111000:d} taka."
print(txt1,"\n")



### :e		-> Scientific format, with a lower case e
import math
r = 10
# Use "e" to convert a number into scientific number format (with a lower-case e):
area = math.pi*r*r
txt = f"The area of the circle is {area:e}"
# txt = f"{area:e}"
print(txt)

## :E		-> Scientific format, with an upper case E




### :f		-> Fix point number format

# Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = f"The price is {45:.2f} dollars."
print(txt)

# without the ".2" inside the placeholder, this number will be displayed like this:
txt = f"The price is {45:f} dollars."
print(txt)




### :F		-> Fix point number format, in uppercase format (show inf and nan as INF and NAN)

# Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = f"The price is {x:F} dollars."
print(txt)

# same example, but with a lower case f:
txt = f"The price is {x:f} dollars."
print(txt)



### :g		-> General format
num = 12345.6789
print(f"The number is {num:g}")

num = 0.000012345
print("The number is {:g}".format(num))


num = 123456789
print(f"The number is {num:g}")

num = 12345.6789
print(f"{num:.3g}")   # 3 significant digits
print(f"{num:.6g}")   # 6 significant digits
print()

## :G		-> General format (using a upper case E for scientific notations)




### :o		-> Octal format

a = 39
#Use "o" to convert the number into octal format:
txt = f"The octal version of {a} is {a:o}"
print(txt)



### :x		-> Hex format, lower case
a = 255
#Use "o" to convert the number into hexadecimal format:
txt = f"The hexadecimal version of {a} is {a:x}"
print(txt)
print()
## :X		-> Hex format, upper case




### :n		-> format numbers according to the current locale(that is, your computer’s regional number settings).
num = 1234567.89
print(f"{num:n}")
print()




### :%		-> Percentage format

a = 0.47
#Use "%" to convert the number into a percentage format:
txt = f"You scored {a:%}"
print(txt)

#Or, without any decimals:
txt = f"You scored {a:.0%}"
print(txt)
print()




### Extra example
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


# Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = f"I want {quantity} pieces of item number {itemno}, at {price:.2f} dollars each -- for a total of {quantity * price} dollars."
print(myorder)


# Index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 24
name = "Hasan"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))