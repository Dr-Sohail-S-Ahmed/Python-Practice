import numpy as np
d = np.arange(30).reshape(2,15)
print(d)

h1,h2,h3 = np.hsplit(d,[6,10])
print(f"h1 array is {h1}")
print(f"h2 array is {h2}")
print(f"h3 array is {h3}")

# v1,v2 = np.vsplit(d,[1])
# print(f"v1 array is {v1}")
# print(f"v2 array is {v2}")