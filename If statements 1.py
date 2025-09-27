temperature = 9
if temperature > 30:    # ':' is used to separate the condition from the code block (as seen with indentations)
    print("It's a hot day") # indentation indicates that this block of code is in fact part of the unindented code above it
    print("Drink plenty of water")  # in other programming languages like JS, C++, etc. code block is added in curly brackets '{}' while in Python the same is done using indentation
elif temperature > 20:  # 'elif' = else if
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:   # 'elif' is used when multiple conditions are to be met while 'else' is used for the last condition
    print("It's chilly")
print("Done")