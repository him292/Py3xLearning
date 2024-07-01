# Polymorphism
# It  allows us to define methods in the child class with the same name as the methods in the parent class.
# This is achieved by overriding the parent class method in the child class.

# method overloading - Doesnt exist in python traditionally ( can only be used with default arguments)

# super() keyworrd is used to call the parent method
# it can call only the immediate parent method, not the grandparent method

# method overriding

# When a method in a subclass has the same name, return type, and parameters
# as a method in its parent class, the subclass method overrides
# the parent class method. When an instance of the subclass
# calls the overridden method, the subclass implementation is
# executed instead of the parent class implementation

class Shape:

    def area(self):
        print("Area of Shape")

class rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    # method overriding
    def area(self):
        return self.length + self.width

class circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = rectangle(10, 20)
print(shape1.area())

shape2 = circle(10)
print(shape2.area())
