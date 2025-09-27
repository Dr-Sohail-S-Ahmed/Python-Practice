# VERY IMPORTANT: It must be ensured that the Python file name shouldn't be the same as any package or module name bcz this can result in error
    # during importing i.e. Python will try to import from the user file of the same name instead of the actual library
# PACKAGE is a collection of related modules organized into a directory (folder) i.e. it's a way to group code logically
    """It's like a game franchise (e.g. The Legend of Zelda) which is a big collection of different yet related games"""
        # Represented by directories (folders) containing '__init__.py' & aren't directly called but modules & subpackages are imported from it
        # e.g. import my_library.module_a
        # From (assumed) directory structure:
            # my_library/
            #     __init__.py
            #     module_a.py
# SUB-PACKAGE is a package contained within a package which organizes modules with a larger package
    """It's like a sub-package series like 2D games or 3D games"""
        # Similar to packages, modules & submodules are imported from it e.g. import my_library.geometry.shapes
        # From (assumed) directory structure:
            # my_library/
            #     __init__.py
            #     geometry/
            #         __init__.py
            #         shapes.py
# MODULE is a single file containing Python code (functions, classes, variables)
    """It's like a specific game in the franchise (e.g. The Legend of Zelda: A Link to the Past) having its own code & content"""
        # To call: import <Module_Name> → import math  |  from <M_N> import <Import_Name> → from math import pi
# SUBMODULE is a module within a module offering more specific functionality
    """It's like a specific part of a game like the 'Inventory system' or 'Combat Mechanics'"""
        # To call: import <M_N>.<SubModule_Name> → import os.path  |  from <M_N> import <SM_N> → from urllib import parse
# CLASS is a blueprint/template for creating objects defining their attributes & methods
    """It's like a character template/class like 'Warrior' or 'Mage' defining what they can do & with what stats"""
        # 1st class defined using 'class' keyword, 2nd instantiate (create object) using <Object_Name> = ClassName()
            # class Dog:
            #     def __init__(self, name):
            #         self.name = name
            # my_dog = Dog("Buddy") #instantiation
# OBJECT is a general term for data structure that has attributes (data) & methods (functions) i.e. everything in Python is an object
    """It's like a 'Potion' that exists as a concept in the game's code having properties (like color or effect) & actions (like being drunk)"""
        # To call: 1st object is created by class, 2nd attributes & methods are accessed with dot notation
            # class Dog:  # Class (Blueprint)
            #     """Represents a dog."""
            #     def __init__(self, name, breed):
            #         self.name = name  # Instance attribute (data)
            #         self.breed = breed  # Instance attribute (data)
            #     def bark(self):  # Method (behavior)
            #         """Simulates a dog barking."""
            #         print("Woof!")
            # # Object and Instance Examples:
            # my_dog = Dog("Buddy", "Labrador")  # my_dog is an object AND an instance of the Dog class.
            # your_dog = Dog("Max", "German Shepherd")  # your_dog is an object AND an instance of the Dog class.
            # # Verification:
            # print(type(my_dog))             # Output: <class '__main__.Dog'> (verifies it's a Dog object/instance)
            # print(isinstance(my_dog, Dog))  # Output: True (verifies it's an instance of the Dog class)
            # print(my_dog.name)              # Output: Buddy (accessing instance attribute)
            # my_dog.bark()                   # Output: Woof! (calling instance method)
            # print(your_dog.name)            # Output: Max (accessing instance attribute)
            # your_dog.bark()                 # Output: Woof! (calling instance method)
# INSTANCE is a specific term which is particular realization of a class i.e. every instance is an object but not every object is an instance
    """It's like 'Red Healing Potion' (which is an instance of Potion class (or a subclass of it) having specific properties (like red color, heals 50HP) & can be used (drunk)"""
        # (same as for Object)
# VARIABLE is a named storage location that holds value
    """It's like 'Health Points (HP)' or 'Experience Points (XP)'"""
        # To call: 1st assign value to variable using '=' operator, 2nd access its value using variable name
            # my_variable = 10
            # print(my_variable)
# METHOD is a function associated with a class defining what an object can do
    """It's like an action a character can perform like 'Attack', 'Cast Spell' or 'Use Item'"""
        # (see Object)
# ATTRIBUTE is a characteristic of an object (or class)
    """It's like a character's property like 'Weapon', 'Armor' or 'Inventory'"""
        # (see Object)


"""THE FOLLOWING IS AN EXAMPLE WHICH EXHIBITS ALL THE IMPORTANT TERMS DEFINED ABOVE
   (IT MIGHT NOT WORK BUT THE PURPOSE IS TO GIVE AN EXAMPLE)"""
    # THIS IS THE DIRECTORY STRUCTURE:
# Package: my_library (represented by the directory structure)
# my_library/
#   __init__.py
#   geometry/    (Sub-package)
#       __init__.py
#       shapes.py   (Submodule)
#   utils.py      (Module)

# my_library/geometry/shapes.py (Submodule)
class Circle:  # Class
    """Represents a circle."""

    pi = 3.14159  # Class variable (attribute)

    def __init__(self, radius):     # special / magic / dunder method '__init__'
        self.radius = radius  # Instance attribute
        self.area = None      # Initialize area attribute

    def calculate_area(self):  # Method
        """Calculates and returns the area of the circle."""
        self.area = self.pi * self.radius**2
        return self.area

# my_library/utils.py (Module)
def greet(name):  # Function (variable in module scope)
    """Greets a person by name."""
    return f"Hello, {name}!"

# main.py (Using the package)
import my_library.geometry.shapes as shapes  # Importing submodule
import my_library.utils as utils  # Importing module

# Using the submodule and class
my_circle = shapes.Circle(5)  # Creating an object (instance of Circle)
circle_area = my_circle.calculate_area()  # Calling a method

# Accessing an attribute
radius_value = my_circle.radius

# Accessing a class variable
pi_value = shapes.Circle.pi

# Using the module and function
greeting = utils.greet("World")  # Calling a function

# Printing the results
print(f"Circle Area: {circle_area}")
print(f"Radius: {radius_value}")
print(f"Pi: {pi_value}")
print(f"Greeting: {greeting}")

#Example of a simple variable.
example_variable = 10;

print(f"Example Variable: {example_variable}")


# CALLING: <Module>.<SubModule>.<Function>
# rolls = numpy.random.randint(low=1, high=6, size=10)
    # What's THIS THING:        type()
    # What CAN I DO WITH IT:    dir()
    # TELL ME MORE:             help()
# EXAMPLE: (copy the following in another file then run to test)
    # import math
    # rolls = math.sqrt(4)
    # print(rolls)
    # print(type(rolls))
    # print(dir(rolls))
    # print(help(rolls.real))

# Special/Magic/Dunder (double underscore) method (like '__init__') are used for operator overloading
# Operator Overloading allows to redefine or specify the behavior of built-in operators (like +, -, *, /, ==, <, etc.)
# Exit Code 0 = Success, Exit Code 1 = General Error or Failure
# (See "For loops - monthwise profit" for very important discussion on value assignment/not found/last element)
# Dunder methods ("__example__") are written when defining a class to tell Python how your objects behave in special situations.
# Normal methods ("example()") are called from outside (by you, not Python) to do explicit work

# 'return' is used inside a function to end the function and give back a value
# 'break' is used inside a (for/while) loop to immediately exit the loop

# .add() and .get() are custom methods while Python’s built-in operators (t['march 6'] = 130 or x = t['march 6']) call upon magic (dunder)
  # methods like __setitem__ & __getitem__ e.g.
  # obj[key] = value → calls → __setitem__(key, value)
  # value = obj[key] → calls → __getitem__(key)
"""This code:
    # def add(self, key, val):
    #     self.data[key] = val
  # ...works with:
    # t = Table()
    # t.add('march 6', 130)
  # ...while this code:
    # def __setitem__(self, key, val):
    #     self.data[key] = val
  # ...works with:
    # t = Table()
    # t['march 6'] = 130
  # ...bcz 1st code is CUSTOM code which works MANUALLY while 2nd one is BUILT-IN which works AUTOMATICALLY
  # ...& also 2nd code is used when we want an object to behave like a dictionary but for custom behavior, we should use custom methods"""
# Analogy: Custom add() is like saying “Please store this manually.” You hand a box to someone and say “Put it in the shelf yourself."
  # ...while __setitem__ is like installing a shelf so you can just slide in any item by key. It automatically puts things where they belong
# (tuple / function call), [list or array / indexing], {dictionary / set}

# 'break' is used inside the loop to exit it while 'return' is used inside the function to end it & optionally give a value

"""
'*' is an unpacking operator i.e. it takes each item from the range & put it directly into a list
a = [range(3)]  # This gives: [range(0, 3)]
print(a)
a = [*range(3)]  # This gives: [0, 1, 2]
print(a)
"""

# Left side (= before) → This is the target (the thing you are defining, creating, or updating).
# Right side (= after) → This is the value/expression already defined somewhere, which will be looked up, calculated, and then stored into the left side.

# self.edges = edges → Take the value from the right side (the parameter edges) and store it in the left side (the object’s attribute self.edges).
# edges = self.edges → Take the value from the right side (the object’s attribute self.edges) and store it in the left side (the local variable edges).
    # Storing in a variable → like writing something on a loose sticky note. It only exists where you wrote it (in that function or scope). Once you leave that place, the note may be gone.
    # Storing in an object’s attribute → like putting that note inside a box (the object) with a label. Now, every time you pick up that box, the note is still inside and travels with the box, no matter where you go in the program.
        # (Variable = Temporary, belongs to a specific place
        # Object's Attribute = Permanent (until deleted), belongs to the object and moves with it

# With respect to single-line comments (with #), Python doesn't consider indentation (as these are considered as notes for humans)...
# ...but when it comes to docstrings (with """), Python considers indentation (as these are considered as official documentation string)

