# OOPS
# Class - Objects
# Constructor
# Self, __init__
# Take input and create class
#     Method
#     # Public, Private, Protected
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation
# Static methods/variables

class Person:
    # attributes
    name = None
    age = None
    city = None
    address = None

    # Behaviour
    def talk(self):
        print("Hello, I can talk")

    def walk(self):
        print("I can walk")

    def sleep(self):
        print("I can sleep")

# at this moment, class is just a blueprint, cannot do anything until we create objects

# Objects creation
# testObj is a reference variable, which holds the address of the object

testObj = Person()
testObj.talk()
testObj.walk()





















