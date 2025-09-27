x = input("First No.: ")
y = input("Second No.: ")
try:
    z = x / int(y)                              # String divided by integer therefore error expected
                                                # More errors can be done to experiment
except Exception as e:
    print("Error name is", type(e).__name__)    # Displays only the name of the error
    print("Error type is", type(e))             # Displays details about the error type like module, class & possibly hierarchy
    print("Error message is", e.args)           # 'args' attribute displays explanation of the error type
    z = None

# This code enables to identify the type of error so that it can be handled accordingly during coding