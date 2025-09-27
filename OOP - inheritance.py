# INHERITANCE in programming means a child can take features from a parent.
# In Python, a child class (also called subclass) can use the properties and methods of a parent class (also called base class) or...
    # ...can also add its own new features or change (override) the parent’s features
        # (Compare with Polymorphism)
# Inheritance allows code reuse, extensibility, readability

# Create a parent class called Vehicle
class Vehicle:
    # Define a method that prints the general use of any vehicle
    def general_usage(self):
        print("general use: transporation")

# Create a child class Car that inherits from Vehicle
class Car(Vehicle):
    # Constructor method runs automatically when Car is created
    def __init__(self):
        print("I'm car")               # Print that this is a car
        self.wheels = 4                # Car has 4 wheels
        self.has_roof = True           # Car has a roof

    # Define a method for specific car usage
    def specific_usage(self):
        self.general_usage()           # Call parent method (general usage)
        print("specific use: commute to work, vacation with family")

# Create another child class MotorCycle that inherits from Vehicle
class MotorCycle(Vehicle):
    # Constructor method runs automatically when MotorCycle is created
    def __init__(self):
        print("I'm motor cycle")       # Print that this is a motor cycle
        self.wheels = 2                # Motor cycle has 2 wheels
        self.has_roof = False          # Motor cycle does not have a roof

    # Define a method for specific motor cycle usage
    def specific_usage(self):
        self.general_usage()           # Call parent method (general usage)
        print("specific use: road trip, racing")

c = Car()                              # Create an object of Car class
m = MotorCycle()                       # Create an object of MotorCycle class

print(issubclass(Car,MotorCycle))      # Check if Car is a child of MotorCycle (returns False)


"""
Docstring:
This program shows inheritance in Python.
- Vehicle is the parent class with a general_usage method.
- Car and MotorCycle are child classes that inherit from Vehicle.
- Each child class has its own constructor and specific_usage method.
- The issubclass check at the end shows whether Car inherits from MotorCycle.
"""

# MULTIPLE INHERITANCE: A child can use the features of multiple parents
'''Method 1'''
class Daddy():
    def gardening(self):
        print("I like gardening")

class Mommy():
    def cooking(self):
        print("I love cooking")

class Kid(Daddy, Mommy):
    def sports(self):
        print("I enjoy sports")

k = Kid()
k.gardening()
k.cooking()
k.sports()

'''Method 2'''
class Father():     # This is "base class"
    # Method to show Father's skills
    def skills(self):
        print("gardening,programming")

class Mother():     # This is "base class"
    # Method to show Mother's skills
    def skills(self):
        print("cooking,art")

# Define a class Child that inherits from both Father and Mother
class Child(Father, Mother):    # This is "derived class"
    # Method to show Child's skills
    def skills(self):
        # Call Father's skills method
        Father.skills(self)
        # Call Mother's skills method
        Mother.skills(self)
        # Add Child's own skill
        print("sports")

# Create an object of Child class
c = Child()
# Call Child's skills method
c.skills()

"""
This program demonstrates multiple inheritance.
The Child class inherits from both Father and Mother classes.
When skills() is called on the Child object, 
it combines Father's, Mother's, and Child's own skills.
"""

# EXERCISE 1
class Animal:   # Create a parent class named Animal
    def __init__(self, habitat):   # Constructor method, runs when object is created
        self.habitat = habitat     # Store the habitat value inside the object

    def print_habitat(self):       # Method to print the animal's habitat
        print(self.habitat)        # Display the stored habitat

    def sound(self):               # Method to print a generic animal sound
        print("Some Animal Sound") # Show the default sound for animals


class Dog(Animal):                 # Create a child class Dog that inherits from Animal
    def __init__(self):            # Constructor for Dog
        super().__init__("Kennel") # Call parent’s constructor & set habitat to "Kennel"

    def sound(self):               # Override parent sound method
        print("Woof woof!")        # Print Dog-specific sound


x = Dog()             # Create a Dog object (this calls Dog’s constructor)
x.print_habitat()     # Call method to print the dog's habitat
x.sound()             # Call method to print the dog's sound


"""
Docstring:
This program shows how inheritance works in Python. 
The Animal class provides common features (habitat and sound). 
The Dog class inherits these features but customizes them:
- It sets its habitat to "Kennel" using super().
- It changes the generic sound into "Woof woof!".
Finally, we create a Dog object and show both its habitat and sound.
"""

# EXERCISE 2
class Teacher:
    def teacher_skills(self):
        print("teach")

class Student:
    def student_skills(self):
        print("learn")

class YouTuber:
    def youtuber_skills(self):
        print("videograph")

class Person(Student,Teacher,YouTuber):
    pass

x = Person()
x.teacher_skills()
x.student_skills()
x.youtuber_skills()