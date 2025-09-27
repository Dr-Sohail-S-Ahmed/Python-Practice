# TUPLES are used for functions that have multiple return values as it holds multiple things together

numbers = (1, 8, 9, 2, 3, 4, 5, 6)  # '[]' are used to define a list while '()' are used to define a tuple
                                    # & they're immuteable i.e. they won't change once created unless edited
                                    # physically from inside the code or appended like a list. Trying to change would give an error.
                                    # However, their values can be reassigned i.e. values swapped
                                    # Tuples don't have append, insert, remove, etc. methods i.e. after '.'
                                    # In Tuple, all values have different meaning (heterogenous)
                                    # In List, all values have similar meaning (homogenous)
print(numbers.index(5))     # gives the location of the first occurance of the number
print(numbers[5])           # gives the number at the location specified
print(numbers)

print("")

numbers = 1, 8, 9, 2, 3, 4, 5, 6    # this is another method of writing tuples i.e. without brackets
print(numbers.index(5))
print(numbers[5])
print(numbers)

print("")

# STUPID PYTHON TRICK (swaps values of tuples but their physical presence remains the same
a = 1
b = 0
a, b = b, a
print(a, b)