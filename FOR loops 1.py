numbers = [2, 3, 4, 5, 6, 8, "X"]   # non-numbers written without quotes will give error
for item in numbers:    # for loop is used to return each entry in a separate line
    print(item)

print(" ")

i = 0
while i < len(numbers): # similar result as above can be attained using the while loop but the code is longer
    print(numbers[i])   # if '[i]' isn't added, Python quotes the entire list equal to the number of items in it otherwise it return 1 item in each row
    i = i + 1

print(" ")

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1      # Alternate method as compared to above