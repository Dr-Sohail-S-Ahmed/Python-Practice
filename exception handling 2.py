# EXCEPTION (see Programming.xlsx > Adv Python)
# Exceptions are like accidents (e.g. dividing by zero or adding number to a string)
# Exception handling is like taking a detour

x = input("First No.: ")
y = input("Second No.: ")
try:                                    # This statement is meant to handle exceptions &...
    z = int(x) / int(y)                 # This alone (without 'try' statement) could generate an error if divided by zero
except Exception as e:                  # Word 'Exception' here isn't a variable but a built-in class to handle general exception errors
    print("Exception error:", e)
    z = None
print("Answer by division is", z)