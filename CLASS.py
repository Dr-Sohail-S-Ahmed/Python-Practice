# See files for reference: "What is CLASS in programming languages.png" & "What is OBJECT in programming languages.png"
# ClASS is like a mould/blueprint while OBJECT is that which is created using this mould
    # '__init__' is a special function used to set initial values for object data and runs automatically when an object is created from the class
    # 'self' is the current object used to store or access data inside the object
# The following is an example of object-oriented programming (OOP) by creating class & 2 Human objects

class Human:
    # 1st method
    def __init__(self, nm, oc):                 # Initializes name & occupation for each Human object + more attributes can also be added
                                                # '__init__(self' is the constructor of an object i.e. invoked automatically
                                                # for new class instances & is necessary for defining the attributes
                                                # 'nm' & 'oc' are the "arguments of a function"
        self.name = nm                          # 1st property (attribute): 'nm' is string
        self.occupation = oc                    # 2nd property (attribute): 'oc' is string
        # Syntax:- self.(attribute) = (value)
        # Variables 'nm' & 'oc' don't exist outside the above code block therefore calling them later in the code would result in an error.
        # Additionally, in order to access the attributes, they must be called upon using 'self' keyword as defined in the initial method

    # 2nd method
    def do_work(self):
        if self.occupation == "tennis player":  # Writing 'oc == "tennis player"' would be incorrect bcz 'self.occupation'
                                                # checks the value of 'occupation' attribute of the object while 'oc' tries
                                                # to use the variable that doesn't exist in this context
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots movies")
        else:
            raise ValueError("Invalid occupation")  # 'ValueError': If occupation is neither of the defined ones

    # 3rd method
    def speaks(self):
        print(self.name, "says, 'How R U?'")

# When defining object, attributes are mentioned after 'self' but when calling those objects mentioning 'self' isn't required
tc = Human("Tom Criuse", "actor")               # 1st object
tc.do_work()                                    # 1st call
tc.speaks()                                     # 2nd call

ms = Human("Maria Sharapova", "tennis player")  # 2nd object
ms.do_work()                                    # 3rd call
ms.speaks()                                     # 4th call

"""A method can be called upon before it's even defined inside a CLASS as the order of the methods doesn't matter so long
as method is defined somewhere in the class & we aren't calling during class definition but only when object is used"""
class Example:
    def first(self):
        return self.second()  # calls method below

    def second(self):
        return "Hello"
