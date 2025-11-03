"""
*****Generators*****

A generator is a special type of function that allows us to generate values one by one, without storing them all in memory.

When a normal function runs — it executes everything and returns a single value.
When a generator function runs — it pauses each time it hits a yield, and resumes from that same spot the next time it's called.

"""
def my_generator():
    print("Start")
    yield 1
    print("Yield 1")
    yield 2
    print("Yield 2")
    yield 3
    print("Yield 3")
    print("End")

gen = my_generator()
# At this point, nothing has executed yet — gen is a generator object.

print(next(gen), "\n")
print(next(gen), "\n")
print(next(gen), "\n")
"""
Each call to next() runs the function until it reaches the next yield.

It remembers its state — so when resumed, it continues after the previous yield.

When there's no more yield, a StopIteration exception is raised automatically

"""

def my_generator():
    print("Start")
    yield 1
    print("Yield 1")
    yield 2
    print("Yield 2")
    yield 3
    print("Yield 3")
    print("End")

gen = my_generator()

# A for loop automatically calls next() for us until the generator is exhausted
for value in my_generator():
    print("Got:", value)
print()


"""
Why use Generators?

Memory efficient        -> Doesn't store all results — produces one at a time.
Lazy evaluation         -> Only computes values when needed.
Infinite sequence   	-> We can build endless data streams safely.
Faster              	-> Less memory overhead for large data.

"""

## *****Infinite Generator*****

def infinite_count(start = 1):
    while True:
        yield start
        start += 1

counter = infinite_count()
for _ in range(5):
    print(next(counter)) # We can keep calling next(counter) forever.
print()


# Another example
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
print()



## *****We can manually iterate through a generator using the next() function:*****
def simple_gen():
    print("This is: ",end = "")
    yield "Nazrul"
    print("This is: ",end = "")
    yield "Yasir"
    print("This is: ",end = "")
    yield "Hasan"
    print("Ended")

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # This will raise StopIteration beacuse after printing the "Ended" there is no next yield
print()

# We can aviod this by using:

def simple_gen():
    print("This is: ", end = "")
    yield "Nazrul"
    print("This is: ", end = "")
    yield "Yasir"
    print("This is: ", end = "")
    yield "Hasan"
    print("Ended")

gen = simple_gen()

print(next(gen))
print(next(gen))
print(next(gen))

try:
    print(next(gen))        # 4th call - generator is exhausted
except StopIteration:
    print("All values yielded. Generator finished gracefully.")
print()




# List comprehension - creates a list
list_comp = [x * x for x in range(5)]       # 0 to 5(excluded)
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)              # That’s just its memory location — nothing has been executed yet
print(list(gen_exp))        # Now it runs the generator — each x*x is calculated one by one and collected into a list.
print()




## *****Difference in memory*****
import sys

list_comp = [x for x in range(1000000)]
gen_exp = (x for x in range(1000000))

print(sys.getsizeof(list_comp))  # Big size
print(sys.getsizeof(gen_exp))    # Very small size
print()




## *****Using a generator expression with sum*****
# Calculate sum of squares without creating a list
total = sum(x*x for x in range(10))
print(total)
print()



## *****Fibonacci Sequence Generator*****
# It can continue generating values indefinitely, without running out of memory

def fibonacci():
   a, b = 0, 1
   while True:
      yield a
      a, b = b, a + b

gen = fibonacci()
for _ in range(100):
   print(next(gen))
print()




## *****Generator Methods*****
# send() method -> allows us to send a value to the generator
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen)                   # Prime the generator
gen.send("Hello")
gen.send("World")
print()

# close() method -> stops the generator
def my_gen():
    try:
      yield 1
      yield 2
      yield 4
    finally:
      print("Generator Closed")

gen = my_gen()
print(next(gen))
gen.close()
# After close(), any further calls to next(gen) will raise StopIteration

