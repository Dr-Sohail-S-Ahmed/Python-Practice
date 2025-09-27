print(10 / 3)   # returns calculated number

print(10 // 3)  # returns integer only

print(10 % 3)   # returns remainder only

print(10 ** 3)  # returns exponent

x = 10
x += 3  # this is the same as 'x = x + 3' & this method is called augmented operator where '=' is assignment operator which is augmented e.g. +=, -=, *=, etc.
print(x)

x = 10  # 'x' is redefined to tell the program the the actual value to 'x' otherwise it'll use the value from the previous calculations
x -= 3
print(x)

x = 10
x *= 3
print(x)

x = 10
x /= 3
print(x)

# IMPORTANT: Understanding how Python's operators work when applied to ints, strings, and lists is no guarantee that you'll be able to...
# ...immediately understand what they do when applied to a tensorflow's Tensor, or a numpy's ndarray, or a pandas's DataFrame
