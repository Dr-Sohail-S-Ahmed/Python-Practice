import time   # import the time module to measure execution time

def time_it(func):   # define a decorator that times how long a function takes
    def wrapper(*args, **kwargs):   # define inner function to wrap the original function
        start = time.time()   # record the start time
        result = func(*args, **kwargs)   # call the original function with given arguments
            # (see Adv Python in Programming.xlsx)
        end = time.time()   # record the end time
        print(func.__name__ + " took " + str((end - start) * 1000) + " mil sec")   # print execution time in milliseconds
        return result   # return the result of the original function
    return wrapper   # return the wrapper function

@time_it   # apply the time_it decorator to measure execution time of calc_square
def calc_square(numbers):   # function to calculate squares of numbers
    result = []   # create an empty list to store results
    for number in numbers:   # loop through each number
        result.append(number * number)   # append the square of the number to the list
    return result   # return the list of squares

@time_it   # apply the time_it decorator to measure execution time of calc_cube
def calc_cube(numbers):   # function to calculate cubes of numbers
    result = []   # create an empty list to store results
    for number in numbers:   # loop through each number
        result.append(number * number * number)   # append the cube of the number to the list
    return result   # return the list of cubes

array = range(1, 100000)   # create a range of numbers from 1 to 99,999
out_square = calc_square(array)   # call calc_square on array and store the result
out_cube = calc_cube(array)   # call calc_cube on array and store the result

"""
This program demonstrates how to use decorators in Python to measure
the execution time of functions. It defines a decorator (time_it) that
records the start and end time of a function, calculates the duration, 
and prints it. The decorator is applied to two functions: calc_square 
(for squaring numbers) and calc_cube (for cubing numbers). The script 
then measures and prints how long each function takes when applied to 
a large range of numbers.
"""
