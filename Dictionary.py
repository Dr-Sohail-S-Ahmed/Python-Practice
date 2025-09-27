# Dictionary (aka Maps, Hashtables, Associate Arrays) enable to store the key value pairs.
# It's like a telephone directory & doesn't store in any specific order.
# Dictionary is added using '{}'.
# Dictionary isn't iterable like list or tuple bcz it's a mapping of keys & values unlike lists or tuples which are ordered sequences
  # therefore Python requires

dict = {"sohail": 325644789, "hamdan": 985547621, "aariz": 45163298}    # all variables are case sensitive
#        key ↑  |  value ↑

# to print entire dictionary
print(dict)

# to print specific associated entry in the dictionary
print("PRINT SPECIFIC")
print(dict["hamdan"])       # '[]' square backets are used to retrieve specific entries from the dictionary

# to add a new entry to an existing dictionary
print("ADD")
dict["shahneela"] = 451236879
print(dict)

# to edit value of an entry in the existing dictionary
print("EDIT")
dict["aariz"] = 100000001
print(dict)

# to delete an entry from an existing dictionary
print("REMOVE")
del dict["sohail"]
print(dict)

# to print all values of the dictionary in separate lines (method 1)
print("PRINT SEPARATE LINES 1")
for entry in dict:
    print("Name:", entry, "No.:", dict[entry])

# to print all values of the dictionary in separate lines (method 2)
print("PRINT SEPARATE LINES 2")
for k,v in dict.items():        # '.items()' is used to iterate over key-value pairs as tuples
  # 'k' (key) & 'v' (value) are temporary variables to be retrieved from dictionary
    print("Name:", k, "No.:", v)

# to check presence or absence of an entry in the dictionary
print("CHECK")
print("shahneela" in dict)
print("saeeda" in dict)

# to clear all entries from the dictionary
print("CLEAR")
print(dict.clear())
print(dict)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
initials = {planet:planet[0] for planet in planets}
print(initials)