def say_hello(name):
    print(f"Okay, {name}")

if __name__ == "__main__":
    print("Running script directly")
    say_hello("Sohail")
# '__name__' is a special built-in variable
# '"__main"' is the default value for '__name__' which signifies that the value is being run directly as the main program
# (see script1.py for details of execution of both these code blocks)
else:
    print("Imported script successfully")