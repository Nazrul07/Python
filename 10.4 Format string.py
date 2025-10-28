'''
This is error

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

We can't combine string and number without fstring
'''

age = 24
txt = f"My name is Nazrul Islam, I am {age}."
print(txt)

price = 50
txt = f"The price is {price} dollars."
print(txt)

price = 24.3843
txt = f"The price is {price:.2f} dollars."
print(txt)

txt = f"The price is {5 * 12} dollars."
print(txt)

