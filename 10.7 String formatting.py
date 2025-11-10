### F-Strings

# F-string allows us to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal.

## Create an f-string
txt = f"The price is 50 dollars."
print(txt,"\n")



## Placeholders
price = 50
txt = f"The price is {price} dollars."
print(txt)
print()


## Modifiers
# A placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type

price = 50
txt = f"The price is {price: .2f} dollars."     # displayed with 2 decimal point
print(txt)


price1 = 22.943
txt1 = f"The price is {price1: .2f} dollars." 
print(txt1)
print()


## Perform Operations in F-Strings
price_per_item = 12.34
txt = f"The price is of 20 iteams is {20 *price_per_item :.2f} dollars"
print(txt)

price = 59
tax = 0.10
txt = f"The price is {price + (price * tax)} dollars"   # Price + txt
print(txt)

# if...else
price = 59
txt = f"It is {'Expensive' if price>60 else 'Cheap'}"
print(txt)
print()



## Execute Functions in F-Strings
fruit = "apple"
txt = f"I love {fruit.upper()}"
print(txt)

txt = f"I love {fruit.capitalize()}"
print(txt)


def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
print()



## More Modifiers
price1 = 59000000
price2 = 1000000220404
txt1 = f"The price is {price1:,} dollars."     # Use a comma as a thousand separator
print(txt1)
txt2 = f"The price is {price2:,} dollars."     # Use a comma as a thousand separator
print(txt2)