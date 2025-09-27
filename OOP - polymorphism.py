# POLYMORPHISM: Different classes can have methods with the same name, but each behaves differently depending on the object
    # (Compare with Inheritance)

class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")

class Goat:
    def sound(self):
        print("Bleat!")

class Cow:
    def sound(self):
        print("Moo!")

# Polymorphism in action
for animal in [Dog(), Cat(), Goat(), Cow()]:
    animal.sound()