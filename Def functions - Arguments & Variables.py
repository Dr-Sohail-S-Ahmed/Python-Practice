total = 0
def sum(a,b):
    print("a =", a)
    print("b =", b)
    total = a + b
    print("Total inside function/code block:", total)   # this total based on the variables defined below
    return total
n = sum(b = 5, a = 3)  # if written as 'sum(5,3)', this is POSITIONAL ARGUMENTS which are considered by default
                       # according to the defined function above but if written as 'sum(b=5,a=3)', this is NAMED
                       # ARGUMENTS which are defined individually outside the defined function code block. If
                       # written as 'sum(5)', this is DEFAULT ARGUMENT which means that the number mentioned will
                       # correspond to the first unknown variable ('a') while the absence of the second number
                       # will automatically assume that the next variable is '0'
print("Total outside function/code block:", total)      # this total is based on the total variable defined
                                                        # outside the code block (on top)
# Despite both 'total' on top (global variable) & 'total' inside defined function (local variable) have exact
# same wording yet the total inside the code block & outside are treated different. This can be confirmed by
# clicking the 'total' word in the print command which highlights the respective 'total' it's referring to

# Triple double quotes (""" or ''') are special comments known as DOCUMENTATION STRINGS used to explain the code
# while '#' is used to create a regular comment
"""
print("SALAM")
"""