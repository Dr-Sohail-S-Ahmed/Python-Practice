import numpy as np

# ELEMENT LOCATION
print("ELEMENT LOCATION")
a = np.array([9,5,1])
print(a[0])     # location of element

# ARRAY DIMENSION
print("ARRAY DIMENSION")
a = np.array([[1,2],[3,4],[5,6]])
print(a.ndim)   # shows dimension of arrays but if any individual element's dimension is changed, error occurs
                # like 'a = np.array([[1,2],[3,4],[5,6,7]])'
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.ndim)   # dimension are represented by '[]'

c = np.array([[[1,2],[3,4]]])
print(c.ndim)

d = np.array([[[[1,2]]]])
print(d.ndim)

# DATA TYPE
print("DATA TYPE")
print(a.dtype)
print(b.dtype)
print(c.dtype)
print(d.dtype)

# BYTE SIZE
print("BYTE SIZE")
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)
print(d.itemsize)

# CHANGING DATA TYPE
print("CHANGING DATA TYPE")
e = np.array([[1,2,3],[4,5,6]], dtype=np.float32)   # data type changed from integer to float and from 64-bit to 32-bit
print(e.itemsize)
print(e)
e = np.array([[1,2,3],[4,5,6]], dtype=complex)      # data type changed to complex nos.
print(e)
            # IMPORTANT NOTE: '...dtype=np.float32' doesn't give error bcz 'float32' is a valid NumPy data type while '...dtype=np.complex' does
            # bcz 'complex' is no longer a valid data type in NumPy + however, this 'complex' (as in '...dtype=np.complex' is built-in
            # Python complex type

# ARRAY SIZE
print("ARRAY SIZE")
print(e.size)       # thru Python
print(np.size(e))   # thru NumPy

# ARRAY SHAPE (AS IN TABLE FORM)
print("ARRAY SHAPE (AS IN TABLE FORM)")
print(e)
print(e.shape)      # thru Python; specifies array height (rows) and width (column)
print(np.shape(e))  # thru NumPy; specifies array height (rows) and width (column)

# RESHAPING ARRAY
print("RESHAPING ARRAY")
print(e.reshape(6,1))   # non-symmetrical shape will give error like changing '(2,3)' to '(4,2)' i.e. all entries should fit the shape

# 1-DIMENSIONAL ARRAY
print("1-DIMENSIONAL ARRAY")
print(e.ravel())    # flatten the array to a single dimension
print(e)            # this show that 'ravel()' doesn't change the original array but rather gives a new one

# CREATING ARRAY FROM SHAPE
print("CREATING ARRAY FROM SHAPE")
print(np.zeros((3,4)))
print(np.ones((3,4)))                    # '0s' and '1s' as in binary + 'ones' and 'zeros' are part of NumPy only
print(2 * np.ones((3,4)))                # '2*', '3*' and their like for numbers beyond '1'
print(np.full((3,4),99))   # '(3,4)' defines the shape of the array while ',99' defines number to be filled in

# RANGE (PYTHON) vs ARANGE (NUMPY)
print("RANGE (PYTHON) vs ARANGE (NUMPY)")
f = range(10)   # in Python + similar to 'range(0,10)'
print(f)

print(np.arange(10))    # in NumPy + similar to 'np.arange(0,10)
print(np.arange(0,10,2))    # 3rd no. indicates the steps

# LINEARLY SPACED NUMBERS
print("LINEARLY SPACED NUMBERS")
print(np.linspace(1,5,10))  # equally spaced nos. btw given starting and ending nos.

# MATHEMATICAL FUNCTIONS
print("MATHEMATICAL FUNCTIONS")
print(b)

print(np.min(b))
print(b.min())      # both give same result

print(np.max(b))
print(b.max())      # both give same result

print(np.sum(b))
print(b.sum())      # both give same result

print(b)
print(np.sum(b,axis=0))
print(b.sum(axis=0))    # both give same result
print(np.sum(b,axis=1))
print(b.sum(axis=1))    # both give same result
# 'axis=0' refers to summing in y-axis while 'axis=1' refers to summing in x-axis

print(np.sqrt(b))       # give square root of all nos. in array

print(np.std(b))        # standard deviation of all nos. in array

print("     For 1-D Array")
g = np.array([1, 2, 3])
h = np.array([4, 5, 6])
result = np.dot(g, h)   # this is matrix product + 'print(g.dot(h))' also gives the same result
print(result)           # Output: 1*4 + 2*5 + 3*6 = 32

print("     For 2-D Array")
i = np.array([[1,2],
              [3,4]])
j = np.array([[5,6],
              [7,8]])
result = np.dot(i,j)    # performs matrix multiplication + 'np.matmul(i,j)' gives the same result
print(result)           # |1 2| |5 6|  =  |(1*5) + (2*7) (1*6) + (2*8)|  =  |19 22|
                        # |3 4| |7 8|     |(3*5) + (4*7) (3*6) + (4*8)|     |43 50|