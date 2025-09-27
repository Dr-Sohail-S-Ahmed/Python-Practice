# Methods are in fact functions attached to an object with '.'
# Even though methods are carried around by all objects of type "list" but Python can't call 'help(method)' directly...
# ...but can do so with its type attach i.e. 'help(list.method) bcz method name only exists with lists. See following examples (remove '#' to test):
# help(append)        # gives error
# help(list.append)   # gives description

x = 4
y = 99
print(x.bit_length())   # Ans: 3 + 'bit_length()' is a method
print(y.bit_count())    # Ans: 4 + 'bit_length()' is a method

# ADD ITEM - 1
print("ADD ITEM - 1")
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(7)   # every objects have functions that showup after '.' is added + append adds the value to the list
print(numbers)

# ADD ITEM - 2
print("ADD ITEM - 2")
numbers = [1, 2, 3, 4, 5, 6]
numbers.append("Bob")
print(numbers)

# INSERT ITEM
print("INSERT ITEM")
numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(3, 100)  # insert is used to add a value to the list + first number denotes the position in the list while the second value denotes that which is to be added at that location
print(numbers)

# REMOVE ITEM
print("REMOVE ITEM")
numbers = [2, 5, 3, 5, 4, 1, 6]
numbers.remove(5)   # remove is used to remove the very first identified value from the list
print(numbers)

# REMOVE ALL ITEMS
print("REMOVE ALL ITEMS")
numbers = [1, 2, 3, 4, 5, 6]
numbers.clear() # removes all items from the list
print(numbers)

# REMOVE LAST ITEM
print("REMOVE LAST ITEM")
numbers = [1, 2, 3, 4, 5, 6]
numbers.pop()   # 'print' function can be used with this to display the removed number
print(numbers)

# LOCATE ITEM
print("LOCATE ITEM")
names = ["Sohail", "Fahad", "Naila", "Saeeda", "Shahneela", "Hamdan", "Aariz"]
print(names.index("Saeeda"))    # identifies the location of an item in the list

# VERIFY ITEM
print("VERIFY ITEM")
numbers = [1, 2, 3, 4, 5, 6]
print(9 in numbers) # in operator is used to check an item in the list & returns 'True' or 'False' + this also avoids error for non-listed items

# TOTAL NUMBER OF ITEMS
print("TOTAL NUMBER OF ITEMS")
numbers = [1, 2, 3, 4, 5, 6, 10]
print(len(numbers)) # returns the total number of entries in a list

# CHANGE 1 ITEM
print("CHANGE 1 ITEM")
numbers = [1, 2, 3, 4, 5, 6]
numbers[1] = "Two"
print(numbers)

# CHANGE >1 ITEM
print("CHANGE >1 ITEM")
numbers = [1, 2, 3, 4, 5, 6]
numbers[:3] = ["I", "II", "III", "XV"]      # it can be seen that selected items can be replaced with same, less or more items
print(numbers)

# SHOW PARTIAL LIST
print("SHOW PARTIAL LIST")
numbers  =  [1,  2,  3,  4,  5,  6,  10]
#            0   1   2   3   4   5   6    <- these are the corresponding positions from left to right
#           -7  -6  -5  -4  -3  -2  -1    <- these are the corresponding positions from right to left
# General syntax is "numbers[start:stop:step]" i.e. start index, end index & increment index (where default is 1)
print(numbers[0:3])         # '0' is first location, '1' is second location, etc.
print(numbers[:3])          # leaving start index gives the same result as above one
print(numbers[3:])          # leaving end index gives the list till the end starting from start index mentioned
print(numbers[-3:])         # this gives last 3 objects
print(numbers[:-3])         # this gives first 4 objects
print(numbers[1:-1])        # this gives the list from start index till just before end index
print(numbers[-1:1])        # this gives blank list bcz slicing occurs in forward direction & the start index is negative
print(numbers[-1:1:-1])     # however, this does give a list in backward direction due to negative step/increment index

# COMBINE LISTS
print("COMBINE LISTS")
numbers = [1, 2, 3, 4, 5, 6, 10]
alphabets = ["a", "b", "c", "d", "e", "f"]
list = numbers + alphabets
print(list)

# LIST WITHIN LIST
print("LIST WITHIN LIST")
within = [["I", "II", "III", "IV", "V"], ["a", "b", "c", "d", "e"], [1.2, 3.4, 5.6, 7.8, 9.0], [10, 20, 30, 40, 50]]
print(len(within))
print(within[-2][1])    # 1st [] calls on the item as list while 2nd [] call the item within that list

# SORTED LIST
print("SORTED LIST")
numbers = [4, 2, 3, 1]
alphabets = ["d", "f", "e", "b", "c", "a"]
print(sorted(numbers))
print(sorted(alphabets))
         # sorting a list with numbers & strings gives error bcz different data types are incompatible for direct comparison
         # e.g. num_alp = ["d", 4, 2, "a", 3, "C", 1, "B"]
    # however, the following can be done to sort the mixed list
num_alp = ["d", 4, 2, "a", 3, "C", 1, "B"]
nums = [x for x in num_alp if isinstance(x, int)]
alps = [x for x in num_alp if isinstance(x, str)]
print(sorted(nums))
print(sorted(alps))     # capital alphabets come before small ones

# MATHS LIST
print("MATHS LIST")
primes = [2, 3, 5, 7, 11]
print(sum(primes))      # sums up list
print(max(primes))      # gives highest value in list

# FLOAT TO INTEGER RATIO
print("FLOAT TO INTEGER RATIO")
x = 0.125
print(x.as_integer_ratio())     # 12.5 x 8 = 100