# PRACTICE EXERCISE
    # 1. Create a decorator function to check that the argument passed to the function factorial is a non-negative integer.
    # 2. Create a factorial function which finds the factorial of a number.
    # 3. Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

import traceback

def check(f):  # define a decorator function "check" that takes another function f
    def helper(x):  # inner function "helper" to validate input before calling f
        if type(x) == int and x > 0:  # check if argument is an integer greater than 0
            return f(x)  # if valid, call the original function with x
        else:
            raise Exception("Argument is not a non-negative integer")  # raise error if invalid
    return helper  # return the helper function to replace the original

@check  # apply the "check" decorator to factorial
def factorial(n):  # define factorial function
    if n == 1:  # base case: factorial of 1 is 1
        return 1
    else:  # recursive case: factorial(n) = n * factorial(n-1)
        return n * factorial(n - 1)

for i in range(1, 10):  # loop through numbers 1 to 9
    print(i, factorial(i))  # print number and its factorial

try:
    print(factorial(-1))  # try factorial of -1 (invalid input)
except Exception as e:  # catch exception
    print(e)  # print exception details

try:
    print(factorial(1.354))  # try factorial of 1.354 (invalid input)
except Exception as e:  # catch exception
    print(e)  # print exception details


"""
This program defines a decorator "check" that ensures only positive integers are passed 
to the factorial function. If invalid input (negative numbers or non-integers) is given, 
an exception is raised. The factorial function is then safely applied to valid inputs.
"""
