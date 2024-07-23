# Encapsulation
# difference between encapsulation and abstraction
def difference_encapsulation_abstraction():
    """Encapsulation and Abstraction are different concepts"""

    print("Encapsulation is a mechanism to encapsulate or wrap the data and functions into a single unit (class).")
    print("Abstraction is a mechanism to hide the implementation details and only show the functionality to the users.")

#Abstraction

from abc import ABC, abstractmethod
# from "folder name" import "class or methods" -  this is to get the data from other files

class Animal(ABC):

    def __init__(self, name):
        self.name = name
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog =  Dog("Buddy")
print(dog.make_sound())

cat = Cat("Whiskers")
print(cat.make_sound())


# another example

class ATB(ABC): # here ABC is abstract class
    @abstractmethod # this is used when you wnat to force a method to be implemented by the child class
    def perform_task1(self):
        """Perform a task"""
        pass
    @abstractmethod
    def perform_task2(self):
        """Get the status of the task"""
        pass

class himanshu(ATB):
    def perform_task1(self):
        print("Performing task 1")

    def perform_task2(self):
        print("Getting the status of task 2")

him = himanshu()
him.perform_task1()

him.perform_task2()