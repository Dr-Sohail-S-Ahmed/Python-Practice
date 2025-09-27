# For skipping the even numbers & printing the square of odd numbers
for sqr in range(1,11):
    if sqr % 2 == 0:
        continue            # this sends the loop back to the beginning without printing anything based on the condition before it + used in both 'for' & 'while' loops
    print(sqr * sqr)

print(" ")

# For skipping the odd numbers & printing the square of even numbers
for sqr in range(1,11):
    if sqr % 2 != 0:          # '!=' means not equal to
        continue
    print(sqr * sqr)