# (see Adv Python in Programming.xlsx)
# Whenever an input is passed using command line (command prompt), it comes to the program as a string therefore any...
# ...number passed should be converted into integer

import argparse   # import argparse module for command-line argument parsing

if __name__ == "__main__":   # check if the script is being run directly
    parser = argparse.ArgumentParser()   # create an ArgumentParser object
    parser.add_argument("--number1", help = "first number")   # define argument for first number
    parser.add_argument("--number2", help = "second number")  # define argument for second number
    parser.add_argument("--operation", help = "operation", \  # define argument for operation type
                        choices=["add","subtract","multiply"])  # restrict valid operations
    # "--" converts the positional argument into optional one i.e. without it arguments must be written in the same order as they're defined
    # ...(e.g. in command prompt "python argument parser.py 4 5 add") but with it, it can be written in any position yet
    # ...the program will run properly e.g. writing in command prompt "python argument parser.py --number2 5 --operation add --number1 4"

    args = parser.parse_args()   # parse the command-line arguments

    print(args.number1)   # print first number (as string)
    print(args.number2)   # print second number (as string)
    print(args.operation) # print chosen operation

    n1 = int(args.number1)   # convert first number to integer
    n2 = int(args.number2)   # convert second number to integer
    result = None   # initialize result variable
    if args.operation == "add":   # check if operation is addition
        result = n1 + n2   # perform addition
    elif args.operation == "subtract":   # check if operation is subtraction
        result = n1 - n2   # perform subtraction
    elif args.operation == "multiply":   # check if operation is multiplication
        result = n1 * n2   # perform multiplication

    print("Result:",result)   # print final result
