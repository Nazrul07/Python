import random

# ***** Integer *****
print(random.randrange(1, 10)) # [1, 10)

# random.randrange(start, stop, step) --> Any number between start to stop divisible by setp.
print(random.randrange(0, 100, 5)) # [0, 100) divisible by 5

print(random.randint(1, 10))   # [1, 10]

# ***** float ***** 
print(random.random()) # [0.0, 1.0)

print(random.uniform(5, 10))  # [5.0, 10.0]

# ***** Random choice *****
fruits = ["apple", "banana", "cherry", "watermalon", "orange"]
print(random.choice(fruits))

# multiple random number set
nums = [1, 2, 3, 4, 5]
test1 = random.choices(nums, k=3) 
test2 = random.sample(nums, k=2)
print(test1)
print(test2[1])

# ***** Suffle *****
cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print(cards)

# ***** Random bits *****
print(random.getrandbits(8))  # 2^8 -> 0–255 range