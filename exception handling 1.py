# If an exception (erro) is like an accident then handling it is like taking a detour

# FOR BUILT-IN EXCEPTIONS
try:
    raise MemoryError("memory error")
except MemoryError as bie:
    print(bie)
"""
Writing the above code as:
try:
    raise MemoryError("memory error") as e:
        print(e)

...will cause an error bcz:
1. 'raise' only throws an exception but it can't bind it to a variable
2. 'except ... as ...:' is a designed syntax for binding the caught exception to a variable (aliasing)
3. 'except ... as ...:' binds exception object to a variable whereas 'raise ... from ...:' doesn't bind but chains new exception to original
"""

# FOR USER-DEFINED EXCEPTIONS
class Custom_Exception(Exception):
# All user-defined exceptions must inherit from "Exception" (or "BaseException") or it won't be treated as an exeption
    def __init__(self, msg):
        self.msg = msg
    def exception_handling(self):
        print("Custom Exception:", self.msg)

try:
    raise Custom_Exception("NOT BUILT-IN ERROR")
except Custom_Exception as ude:
    ude.exception_handling()

# FINALLY KEYWORD
def process_file():
    try:
        f = open("C:\\Users\\Admin\\PycharmProjects\\PYTHON PRACTICE\\example.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up resources...")
        f.close()

process_file()

"""
-The keyword "finally" is used for guaranteed cleanup i.e. the code still runs no matter what happens
-It's purpose is resource management i.e. closing files, releasing locks, disconnecting from databases, cleaning up GPU memory in ML, etc
-The keyword "finally" always comes after "try" in the following combinations:
a) try ... finally
b) try ... except ... finally
c) try ... except ... else ... finally
"""

# PRACTICE EXERCISE
    # Create: (i) custom exception AdultException,
            # (ii) class Person with name & age,
            # (iii) function get_minor() in the class which throw exception if adult else returns age
            # (iv) function display() which prints age & name of person
class AdultException(Exception):
    pass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_minor(self):
        if int(self.age) >= 18 or int(self.age) <= 0:
            raise AdultException
        else:
            return print(f"Minor Age -> {self.age}")
    def display(self):
        try:
            print(f"Age -> {self.get_minor()}")
        except AdultException:
            print("This person is an adult.")
        finally:
            print(f"Name -> {self.name}")

Person("Hamdan",11).display()
Person("Sohail",44).display()
Person("Hamdan",11).get_minor()
Person("Sohail",44).get_minor()