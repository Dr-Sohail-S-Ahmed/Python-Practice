def late_latif(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order < len(arrivals) -1

arrivals = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
print(late_latif(arrivals,"vwx"))   # prints late after half have arrived excluding the last one

for arrival in arrivals:
    print(arrival, "")          # for both list & tuple: prints all in column
for arrival in arrivals:
    print(arrival, end="")      # for both list & tuple: prints all in row + "" can be used to include space after each item

print("")

# TO PRINT UPPERCASE LETTERS ONLY
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
for char in s:
    if char.isupper():
        print(char, end='')

print("")

# FOR LOOP
for i in range(10):
    print(i, "", end="")

print("")

# List Comprehension: It's like a shortcut for making new list (meeting certain conditions) out of old one in single line compact code/syntax
# [referred to from Lists.py]
squares = [n**2 for n in range(10)]
print(squares)

planets = ['venus', 'jupiter', 'mars', 'earth']
shortest =       [planet.upper()     +    '!'     for     planet  in  planets if len(planet) < 6 and len(planet) > 4]
#  what's added in upper case ↑ | addition ↑ | iterating list ↑   |   ↑ list  |   ↑ condition 1  |    ↑ condition 2
print(shortest)

# (or can also be written as the following i.e. to improve readability)
planets = ['venus', 'jupiter', 'mars', 'earth']
shortest = [planet.upper() + '!'
            for planet in planets
            if len(planet) < 6 and len(planet) > 4]
print(shortest)

print("")

    # (same as above but without list comprehension)
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

print("")

# (defining a function...)
nums = [5, -1, -2, 0, 3, -0.5]
def count_negatives(nums):
    return len([num for num in nums if num < 0])
print(count_negatives(nums), "nos. are negative")    # mentions the quantity of the -ve nos.

# (this gives total number of TRUE & FALSE)
def count_neg(nums):
    return len([num < 0 for num in nums])
print(count_neg(nums))

print("")


# WHILE LOOP
i = 0
while i < 10:
    print(i, "", end="")
    i += 1      # this is the same as 'i = i + 1'

print("")

