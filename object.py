# Understanding OBJECT
"""It's a self-contained unit that bundles together data (attributes) and behavior (methods) (like a big thing having characteristics & actions)
Attributes like color, make, model, current speed
Methods (functions attached to an object) like start engine, accelerate, brake, turn"""
# The following code shows the examples of object:
class Car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        self.speed = 0  # Initial speed

    def start_engine(self):
        print("Engine started!")

    def accelerate(self, amount):
        self.speed += amount
        print(f"Accelerating to {self.speed} mph")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"Braking to {self.speed} mph")

# Creating a Car object (an instance of the Car class)
my_car = Car("Red", "Toyota", "Camry")

# Accessing attributes
print(f"My car is a {my_car.color} {my_car.make} {my_car.model}")

# Calling methods
my_car.start_engine()
my_car.accelerate(30)
my_car.brake(10)

