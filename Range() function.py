numbers = range(8)
print(numbers)      # this will only generate range showing starting & ending numbers beginning with '0'

print("***")

for number in numbers:  # mentions all numbers starting from 0
    print(number)       # this will generate all 8 numbers from 0-7 in separate rows

print("###")

numbers = range(4, 10)   # first number = starting number, second number = ending number
for number in numbers:
    print(number)       # this will generate number range between the starting & ending numbers mentioned (excluding the ending number)

print("|||")

numbers = range(4, 13, 2)   # first number = starting number, second number = ending number, third number = numbers to be skipped
for number in numbers:
    print(number)           # this will generate number range between the starting & ending numbers but skipping 2 numbers before printing the next number
