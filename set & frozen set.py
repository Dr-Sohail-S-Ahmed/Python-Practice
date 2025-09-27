# PRACTICE EXERCISES

# SET & FROZEN SET
# create a normal set
my_set = {1, 2, 3, 4}

# convert it into an immutable set (frozenset)
frozen = frozenset(my_set)

print("Original set:", my_set)
print("Frozen set:", frozen)

# try to modify frozenset
try:
    frozen.add(5)  # this will raise an error
except AttributeError as e:
    print("Error:", e)


# DIFFERENCE BETWEEN SETS
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Original sets: {set1} and {set2}")
print(f"Difference of set1 and set2 using difference(): {set1.difference(set2)}")
print(f"Difference of set2 and set1 using difference(): {set2.difference(set1)}")
print(f"Difference of set1 and set2 using '-' operator: {set1 - set2}")
print(f"Difference of set2 and set1 using '-' operator: {set2 - set1}")