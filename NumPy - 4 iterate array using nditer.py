import numpy as np

nd = np.arange(21).reshape(3,7)
print(nd)

# .nditer iterates over elements more efficiently & flexibly in any order

print("nditer - Array in Fortran-style")
for x in np.nditer(nd, order='F'):     # 'x' is NumPy array scaler i.e. it's a single value from NumPy array represented as NumPy object (not a standard Python scalar like 'int' or 'float')
    print(x)                           # 'print(x, end=" ")' would print array with gaps

print("nditer - Array Columns in Fortran-style")
for x in np.nditer(nd, order='F', flags=['external_loop']):
    print(x)

print("nditer - Modify Original Array")
for o in np.nditer(nd, op_flags=['readwrite']):     # 'o' is NumPy array scalar + nditer iterator allowed both read & write
    o[...] *= 10                                    # '...' is special way to access value of current element within the iterator
print(nd)

print("nditer - Iterate Thru Multiple Arrays Simultaneously")
nd = np.arange(21).reshape(3,7)
ma = np.arange(3,15,4).reshape(3,1)
print(nd)
print(ma)
# nd & ma should both be broadcastable i.e. either their shapes should be same or at least on of their dimensions should be same
for a,b in np.nditer([nd,ma]):      # 'a' hold current element from 'nd' while 'b' holds current element from 'ma'
    print(a,b)