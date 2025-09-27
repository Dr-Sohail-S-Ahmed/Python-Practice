x = input("First No.: ")
y = input("Second No.: ")
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:              # 'ZeroDivisionError' is specifically meant to handle division by zero
    print("Division by zero not allowed")   # No need to add variable 'e' here
    z = None                                # No need to write 'print("Answer by division is", z)'