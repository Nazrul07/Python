## Difference --> Substraction
# -> The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# -> Keep all items from set1 that are not in set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)

print(set3)

# -> We can use the - operator instead of the difference() method, and we will get the same result.
set4 = set1 - set2
print(set4)
print()

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1.difference_update(set2) # Shortcut -> (-=)
print("Updated set1 after difference_update:", set1)
print()



## Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets. --> XOR operation
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)

print(set3)

# we can use the ^ operator instead of the symmetric_difference() method, and we will get the same result.
set4 = set1 ^ set2 # The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
print(set4)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2) # Shortcut -> (^=)

print(set1)