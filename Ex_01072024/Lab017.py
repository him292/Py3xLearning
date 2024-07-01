# Inheritance
# acquiring properties and behaviour from parent

# single level (mostly used)
class Parent:
    house_key = "abc@123"
    def a(self):
        print("Parent class")

class Child(Parent):
    def b(self):
        print("Child class")

child = Child()
child.a()
child.b()
print(child.house_key)

# multiple inheritance (used rarely) - multiple child inheriting from one parent
class Father:
    def Father_money(self):
        return "Father class"

    def home(self):
        return "Fathers home"

class Mother:
    def Mother_money(self):
        return "Mother class"

    def home(self):
        return "Mother's home"

class Child(Father, Mother):
    def Child(self):
        return "Child class"

    def home(self):
        return "Child's home"

child = Child()
print(child.Father_money())
print(child.Mother_money())
print(child.home()) # since there are multiple home() in the code, when called, home() will be called
# of child's class, as this is local to child

# In java, its the diamond problem, when multiple inheritance is used, and both the parent classes have same method,
# then which method to call, java doesnt know, so it gives error, to avoid this, we use super() keyword, which calls
# the method of parent class, which is being inherited by child class

# Python solved it by: ( MRO - method resolution order) : which means, whichever class comes first in the order, will be executed

# if we want to call Fathers home() method, then
# class Child1(Father, Mother):
#
# # if mother's home() method:
# class Child2(Mother, Father):
