a = "Hello, World!"
b = '''
Hello World..!
This is Python.
'''
print(a.upper()) # the whole string
print(b.upper())

a = "hello, world!"
print(a.capitalize()) # Only for 1st position
print(a.lower())


a = " Hello, World! "
print(a.strip()) # removes any whitespace from the beginning or the end

x1 = "Hello, World!"
print(x1.replace("H", "J")) # to replace
print(x1.replace("Hello", "Python"))

# spliting
x2 = "This is AI era"
print(x2.split())

x3 = "Python, is, easy"
print(x3.split("is"))