# ':' along with white space is used to identify that the code block has begun
# '>>>' is used for testing small pieces of code, interactive exploration, debugging, learning, quick calculations
# Using """ for docstrings: Python is still able to parse (analyze & breakdown) them therefore can give an error when code is run
# However, using ``` (triple backticks) within the docstrings enables Python to clearly delineate code examples within your documentation

# The following defines a function of dividing candies equally btw 3 frnds while smashing those which can't be divided
def to_smash(total_candies, n_friends=3):
    """
    Function to determine how many candies are left after splitting them among friends.
    Prints the number of candies being split and returns the remainder.
    """
    # THIS FOLLOWING CODE...
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")

    # ...IS SIMILAR TO THIS ONE
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

    # Return the remainder after splitting candies among friends
    return total_candies % n_friends

# Test cases
print(to_smash(91))                          # Output: Splitting 91 candies, Splitting 91 candies, 1
print(to_smash(3))                           # Output: Splitting 1 candy, Splitting 1 candy, 1
print(to_smash(10, 4))    # Output: Splitting 10 candies, Splitting 10 candies, 2