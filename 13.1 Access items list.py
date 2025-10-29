thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "grape", "peach"]

# Using loop to access all the items of the list
for i in range(len(thislist)):
    print(f"Item {i}:", thislist[i])
print()

## Direct access
print("Direct access:")
print("2nd item:", thislist[1])
print()

## Negative Indexing
print("Negative Indexing")
print("Last item:", thislist[-1])
print(thislist[-4:-1])
print(thislist[-4:])
print(thislist[:-4])             # all items except last 4 items
print(thislist[-len(thislist):]) # all items from first to last
print()

## Range of Indexes
print(thislist[2:5])
print()

for item in thislist[2:5]:  # indexes 2, 3, 4 → 3rd to 5th items
    print(item, end = " ")
print()
print()

print(thislist[:4]) # 1st to 4th items
print(thislist[3:]) # 4th item to last item

# To determine if a specified item is present in a list use the in keyword
if "banana" in thislist:
    print("Banana is in the list")
else:
    print("Banana is not in the list")