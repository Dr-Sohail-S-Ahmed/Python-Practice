# Numpy main objective is 'n' dimensional array (ndarray)

# DISPLAY LIST OF FUNCTIONS
import numpy as np
print(dir(np))

# CREATE ARRAY
A = np.array([1,2,3])       # this is similar to Python list written as 'A = [1,2,3]' and indexing can be done in similar fashion
print(A)

# Benefits of using 'Numpy Array' over 'Python List': Less memory, Faster, Convenience

import time
import sys

# MEMORY USAGE
print("MEMORY USAGE")
    # Python range
l = range(1000)     # range of 1000 elements
print(sys.getsizeof(1) * len(l))        # find size of an integer multiplied by the total length of the range
    # Numpy array
array = np.arange(1000)
print(array.itemsize * array.size)      # find size of single item multiplied by the total length of the array


# TIME TAKEN
print("TIME TAKEN")
size = 1000000      # don't increase number to billion as this could hang the computer

    # Python range
L1 = range(size)
L2 = range(size)

start = time.time()
result = [x+y for x,y in zip(L1,L2)]        # 1st elements of each list are added and added to the list then same for 2nd and so on
    # ↑ this is list comprehesion
print("Python list took: ", (time.time()-start) * 1000, "ms")

    # Numpy array
A1 = np.arange(size)
A2 = np.arange(size)

start = time.time()
result = A1 + A2        # Numpy syntax is simpler, doesn't require list comprehension and adds arrays directly without explicit loop
print("Numpy array took: ", (time.time()-start) * 1000, "ms")

# KEY TAKEAWAYS:
# Numpy is created in low-level programming language 'C',
    # Requires more memory (than 'range' objects) as all elements are stored in memory,
    # Compared to Python lists, it's more memory-efficient for certain data types and operations,
    # It has fixed data type for their elements (e.g., int64), which allows for faster computations
# Python converts 'range' objects to lists for numerical operations,
    # It's list comprehension performs looping and operations which are much slower,
    # It take up less memory space but is less efficient than Numpy,
    # It's list comprehension makes the syntax more complex,
    # It's lists can contain elements of different data types which makes it MORE FLEXIBLE BUT LESS EFFICIENT FOR NUMERICAL WORK


# TESTING SIMPLE NUMPY ARRAY SYNTAX:
print("TESTING SIMPLE NUMPY ARRAY SYNTAX")

T1 = np.array([1,2,3])
T2 = np.array([4,5,6])

print(T1 + T2)
print(T1 - T2)
print(T1 * T2)
print(T1 / T2)