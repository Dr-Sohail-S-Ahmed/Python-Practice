# Defined three simple functions
def greet():
    print("Hello!")
def bye():
    print("Goodbye!")
def surprise():
    print("Boo!")
print("Top-level code: toy.py has been loaded")
# Prints the value of the __name__ variable so you can tell whether the file is being executed directly or imported, before the main guard runs
print(__name__)
# Only run these when the file is executed directly
if __name__ == "__main__":
    print("Running directly, so calling greet() and bye()")
    greet()
    bye()
