import numpy as np

# INDEXING
print("INDEXING")
a = np.array([[1,2,3],   # this is 1st row numbered '0'
              [4,5,6],   # this is 2nd row numbered '1'
              [7,8,9]])  # this is 3rd row numbered '2'
            #  ↑ ↑ ↑
            #  ↑ ↑ this is 3rd column numbered '2'
            #  ↑ this is 2nd column numbered '1'
            #  this is 1st column numbered '0'
print(a)
print(a[1,2])       # '[row_index, col_index]' + print from 2nd row and 3rd column
print(a[0:2,2])     # from 1st to 2nd row print 3rd column
print(a[2,0:2])     # from 3rd row print 1st to 2nd column
print(a[-1,0:2])    # from last row print 1st to 2nd column + same answer as '[2,0:2]'
print(a[:,1:3])     # from all rows print 2nd to 3rd column

# ITERATING THRU ARRAY
print("ITERATING THRU ARRAY")
for row in a:
    print(row)      # simply prints array row-wise like a list

# FLATTENING LIST
print("FLATTENING LIST")
fl = np.arange(12).reshape(3,4)
print(fl)
for row in fl:           # to iterate thru rows
    print(row)           # prints each row of the table separately

print("Method 1 (Python)")
for row in fl:
    for cell in row:    # to iterate thru every element
        print(cell)     # prints each element of the table separately

print("Method 2a (NumPy)")
for cell in fl.flat:
    print(cell)     # flattens the list into a single dimensional array
# .flat() is 1D iterator over elements of array (instead of creating new flattened list), just allows access to array (doesn't create new)

print("Method 2b (NumPy)")
for cell in fl.flatten():
    print(cell)             # shorter syntax (than Python) to print each element of the table separately
# .flatten() is a method which returns new array in 1D format while original array remains unchanged
# .flatten() = .flatten(order="C") = .flatten(order="c") -> is default (row-major order) i.e. left to right & top to bottom
# .flatten(order="F") or .flatten(order="f") is Fortran-style (column-major order) i.e. top to bottom & left to right
# .flatten(order="A") or .flatten(order="a") is automatic i.e. preserves original order which maybe row-major or column-major
# .flatten(order="K") or .flatten(order="k") is preserve memory layout (used for performance optimization) i.e. behaves "C" & "F" as...
# ...the original array was & also tries to keep the same order while keeping the original structure intact (see example below)

print("Method K (NumPy)")
print(fl)

sliced_fl = fl[:, ::2]         # ':' denotes all rows selected while '::2' (array[start:stop:step]) denotes step/skip size
print("K → Sliced Non-Contiguous Array")    # Contiguous Array: Whose elements are stored in the memory without gaps (for faster processing)
print(sliced_fl)

print("K → Flattened with K-order")
print(sliced_fl.flatten(order="K"))

# STACKING ARRAYS
print("STACKING ARRAYS")
b = np.arange(6).reshape(3,2)
c = np.arange(6,12).reshape(3,2)
print(b)
print(c)

print(np.vstack((b,c)))     # stacks 'b' over 'c' as if it's a single array
print(np.hstack((b,c)))     # stacks 'c' on right of 'b'
    # double brackets used here bcz it require tuple or list of arrays i.e. merging multiple arrays require grouping together

# SLICING ARRAYS
print("SLICING ARRAYS")
d = np.arange(30).reshape(2,15)
print(d)

print(np.hsplit(d,3))   # splits array horizontally stacked arrays
hor = np.hsplit(d,3)
print(hor[0])
print(hor[1])
print(hor[2])

print(np.vsplit(d,2))   # splits array vertically stacked arrays
ver = np.vsplit(d,2)
print(ver[0])
print(ver[1])

    # single bracket used here bcz 1 array is split into multiple arrays

# INDEXING WITH BOOLEAN ARRAYS
print("INDEXING WITH BOOLEAN ARRAYS")
e = np.arange(12).reshape(3,4)
print(e)

con = e > 5
print(con)      # prints boolean value for condition specified in variable 'con'
print(e[con])   # extracts only that part of array that meets the condition in variable 'con'
e[con] = 69     # replaces all the element in the array with another number + string can't be printed instead bcz NumPy requires same data type
print(e)

# cont 4th vid