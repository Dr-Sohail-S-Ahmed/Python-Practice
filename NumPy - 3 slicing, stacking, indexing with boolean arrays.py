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

print(np.vstack((b,c)))     # stacks 'b' over 'c' as if it's a single array + must be written as a tuple
print(np.hstack((b,c)))     # stacks 'c' to right of 'b' + must be written as a tuple
    # double brackets used here bcz it require tuple or list of arrays i.e. merging multiple arrays require grouping together

# SLICING ARRAYS
print("SLICING ARRAYS")
d = np.arange(30).reshape(2,15)
print(d)

print(np.hsplit(d,3))   # equally splits array as horizontally stacked arrays
hor = np.hsplit(d,3)
print(f"Horizontal array 1 is {hor[0]}")
print(f"Horizontal array 2 is {hor[1]}")
print(f"Horizontal array 3 is {hor[2]}")
    # single bracket [] used here bcz 1 array is split into multiple arrays

h1,h2,h3 = np.hsplit(d,[6,10])
    # split at 7th & 11th positions horizontally + if split position is absent in array, 1 array appears empty
    # writing "h1,h2,h3 = np.hsplit(d,[6])" would give ValueError bcz 3 arrays are expected but only 1 split position is given
print(f"h1 array is {h1}")
print(f"h2 array is {h2}")
print(f"h3 array is {h3}")

print(np.vsplit(d,2))   # equally splits array as vertically stacked arrays
ver = np.vsplit(d,2)
print(f"Vertical array 1 is {ver[0]}")
print(f"Vertical array 2 is {ver[1]}")
    # single bracket [] used here bcz 1 array is split into multiple arrays

v1,v2 = np.vsplit(d,[1])    # split at 2nd position vertically + if split position is absent in array, 1 array appears empty
print(f"v1 array is {v1}")
print(f"v2 array is {v2}")

# INDEXING WITH BOOLEAN ARRAYS
print("INDEXING WITH BOOLEAN ARRAYS")
e = np.arange(12).reshape(3,4)
print(e)

con = e > 5
print(con)      # prints boolean value for condition specified in variable 'con'
print(e[con])   # extracts only that part of array that meets the condition in variable 'con'
e[con] = 69     # replaces all the element in the array with another number + string can't be printed instead bcz NumPy requires same data type
print(e)

# FINDING EXTREMITIES & SPECIFIC VALUES
print("FINDING EXTREMITIES")
print(f"MAX value: {e.max()}")  # gives maximum value in array
print(f"MIN value: {e.min()}")  # gives maximum value in array
print(f"MAX value index: {np.argmax(e)}")    # gives maximum value position in array
print(f"MIN value index: {np.argmin(e)}")    # gives minimum value position in array

transactions = np.array([[101, 'Mohan', 250.50, '2023-08-01'],
                        [102, 'Bob', 150.00, '2023-08-02'],
                        [104, 'David', 400.20, '2023-08-03'],
                        [103, 'Fatima', 300.75, '2023-08-01'],
                        [105, 'Aryan', 310.1, '2023-08-04']])
print(f"All transaction values: {transactions[:,2]}")   # ':' means all values, '2' means 3rd column
print(transactions[:,2].dtype)      # data type
print(transactions[:,2].astype(float))      # converted to float
print(f"All transaction values as float: {transactions[:,2]}")

trans_index = np.argmax(transactions[:,0])  # finds position of maximum value in given column
print(f"Max transaction location: {trans_index}")
print(f"Data of maximum transaction: {transactions[trans_index]}")    # using transaction index to find array of data
print(f"Specific transaction: {transactions[transactions[:,0] == "102"]}")   # "102" is in Unicode 32 string

# CONSIDERING THESE PRACTICAL EXAMPLES:
print("PRACTICAL EXAMPLE 1")    # sales, revenue, discounts, etc.
q1 = np.array([[200,220,250],   # Q1 sales for Product A for 3 regions
               [150,180,210],   # Q1 sales for Product B for 3 regions
               [300,330,360]])  # Q1 sales for Product C for 3 regions
q2 = np.array([[209,231,259],   # Q2 sales for Product A for 3 regions
               [155,192,222],   # Q2 sales for Product B for 3 regions
               [310,340,375]])  # Q2 sales for Product C for 3 regions
print(q1+q2)        # total sales of products from Q1 & Q2
print(q1-q2)        # difference in sales of products from Q1 & Q2
print((q2-q1)/q1*100)   # %age growth in sales of products fromm Q1 & Q2

prices = np.array([[10,12,11],      # prices of product A for 3 regions
                   [8,9,10],        # prices of product B for 3 regions
                   [15,16,17]])     # prices of product C for 3 regions
q1_rev = q1 * prices
q2_rev = q2 * prices

print(q1_rev)    # Q1 revenues
print(q2_rev)    # Q2 revenues

q1_disc = q1_rev * 0.1
q2_disc = q2_rev * 0.1

print(q1_disc)  # Q1 discounts
print(q2_disc)  # Q2 discounts

q1_net_rev = q1_rev - q1_disc
q2_net_rev = q2_rev - q2_disc

print(q1_net_rev)   # Q1 net revenues
print(q2_net_rev)   # Q2 net revenues

print(np.sum(q1_disc))      # Q1 total discounts
print(np.sum(q2_disc))      # Q2 total discounts