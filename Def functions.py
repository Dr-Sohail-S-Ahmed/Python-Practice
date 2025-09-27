# When after defining a function, "return" statement isn't used, a special value is displayed "None" (which is similar to "null" in other programming languages)
# This means that the function might be working but nothing can be returned
# However, it must be remembered that "return" statement is used where computation & returning a value is intended whereas where only printing something is required this statment isn't required
# "Higher-order functions" are the functions that operate on other functions i.e. functions are supplied as arguments to other functions

tom_list = [100, 200, 300, 400, 500]
dick_list = [600, 700, 800, 900]
harry_list = [1000, 1100, 1200]

# The following is a longer method of finding total of numbers in different list but is impractical for
# multiple lists in dozens or hundreds
total = 0
total = sum(tom_list)
print("Tom's Expense List:", total)
total = 0
total = sum(dick_list)
print("Dick's Expense List:", total)
total = 0
total = sum(harry_list)
print("Harry's Expense List:", total)

# The following is a much more compact code to get the above result
def calculate_total(exp):       # 'Def' = Define a name for the function. (see Bard explanation to complete)
                                # Whatever is written under indentation of 'def' will be considered part of
                                # the function that's defined. This code block will always run when this function
                                # is called. Additionally, after defining the function name '()' can be left empty.
                                # However, in this case 'exp' is added bcz this will be used in the For loop below.
    total = 0
    for e in exp:
        total = total + e
    return total                # This will only create a result but won't display it

# The following will enable the defined function above to be used for specific list on top without additional code
print("Tom's Expenses:", calculate_total(tom_list))
print("Dick's Expenses:", calculate_total(dick_list))
print("Harry's Expenses:", calculate_total(harry_list))
# Although this code is shorter but separate print command is required for each list