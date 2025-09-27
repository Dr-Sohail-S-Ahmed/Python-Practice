profit = [2000, 3000, 4000, 5000, 6000]
total = 0
profit = profit[0] + profit[1] + profit[2] + profit[3] + profit[4]
print(profit)

print(" ")

# This will give the same result as below: total = profit[0] + profit[1] + profit[2] + profit[3] + profit[4]

# this code is much more compact & doesn't require repetition but gives result after every addition therefore
# giving multiple answers till the loop ends
profit = [2000, 3000, 4000, 5000, 6000]
total = 0
for item in profit:
    total += item
    print(total)

print(" ")

# to print range of numbers. 'Range' is already a function in Python therefore no need to define it separately
for x in range(1,11):
    print(x)

print(" ")

# to print number squared
for i in range(1,11):
    print(i*i)