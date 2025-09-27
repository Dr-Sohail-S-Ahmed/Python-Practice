# 3 types of data: integer/float, boolean & string
names = ["Sohail", "Ali", "Imran", "Sadiq", "Umair"]    # square brackets '[]' can be used to write lists
print(names)

names = ["Sohail", "Ali", "Imran", "Sadiq", "Umair"]
print(names[-2])  # Python begins a series with '0' & the number in '[]' will print object at that number. -1 would give the last object in the list. Negative number list doesn't begin from '0' but from '-1'

names = ["Sohail", "Ali", "Imran", "Sadiq", "Umair"]
names[3] = "Kashif"  # Correction can be done in this manner as well in order to the edit the list
print(names)

names = ["Sohail", "Ali", "Imran", "Sadiq", "Umair"]
print(names[0:2])   # to print only the initial values in the list number range is written in '[]' & this new list will end before the range end number i.e. '[0:3]' will return values upto 2 while excluding 3

"""A mutable object can be changed after it's created. You can modify its internal state without creating a new object.
   Analogy: On whiteboard, one can write as much as one wants & can change also but a new whiteboard isn't created for changes
   Examples: LISTS (e.g., [1, 2, 3]), DICTIONARIES (e.g., {"name": "John"}), SETS (e.g., {1, 2, 3})"""

"""An immutable object cannot be changed after it's created. If you try to modify an immutable object, Python creates a new object with the changed value.
   Analogy: On printed book nothing can be changed & in order to make changes a new book must be printed
   Examples: INTEGERS (e.g., 5), FLOATS (e.g., 3.14), BOOLEANS (e.g., True, False), STRINGS (e.g., "hello"), TUPLES (e.g., (1, 2, 3))"""

# List Comprehension: It's like a shortcut for making new list (meeting certain conditions) out of old one in single line compact code/syntax
# (see examples in PRACTICE_calling from list & tuple.py)