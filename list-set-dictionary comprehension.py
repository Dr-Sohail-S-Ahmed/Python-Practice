# PRACTCE EXERCISES: List, Set, Dictionary Comprehensions

# 1. Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict
    # Example :
    # integer = [0, 1, 2, 3, 4]
    # binary = ["0", "1", "10", "11", "100"]
    # Ans: binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = {int:bin for int,bin in zip(integer,binary)}
print(binary_dict)

# 2. Create a List which contains additive inverse of a given integer list
# An additive inverse `a` for an integer `i` is a number such that: a + i = 0
    # Example:
    # integer = [1, -1, 2, 3, 5, 0, -7]
    # Ans: additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

integers = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1*i for i in integers]
print(additive_inverse)

# 3. Create a set which only contains unique sqaures from a given a integer list.
    # integerz = [1, -1, 2, -2, 3, -3]
    # Ans: sq_set = {1, 4, 9}

integerz = [1, -1, 2, -2, 3, -3]
sq_set = {i*i for i in integerz}
print(sq_set)       # gives only unique set of squares i.e. "2 x 2" & "-2 x -2" both answer is "4" therefore "4" only mentioned once