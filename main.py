# (see also Programming.xlsx)
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':      # This means only run the 'print_hi()' function if this file is being run directly
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Python gives every file a special built-in variable called '__name__'
    # If you run the file directly, '__name__' becomes '__main__'
    # If the file is imported into another file, __name__ becomes the file's name
# ANALOGY: Imagine you have a machine with a Start button...
    # If you press the Start button yourself, the machine begins working → like running the file directly
    # If someone else connects your machine as part of their big machine, then your Start button won’t do anything...
    # ...unless they tell it to run → like importing
    # i.e. "Self-start = executed directly" & "Controlled start = imported into something else"