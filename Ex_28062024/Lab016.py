# web automation - Selenium
# login page

# class VWOLoginPage:
#     email = None
#     password = None
#
#     # below constructor is setting the values for email and password
#     # so that we can use them in the methods
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
#
#     def login_confirm(self):
#         if self.password == 'pass123':
#             print('Login successful')
#         else:
#             print('Login failed')
#
#
# user = VWOLoginPage('user@example.com', 'pass123')
# user.login_confirm()
#
#
# # Encapsulation - bind the data variables with the methods
# # wrapping/hiding of the data - data binding
# # Hide the data members(class variables, instance variables) by using only methods
#
# class Car:
#     name = None
#     password = '123'
#
#     def __init__(self):
#         print("I am called when a object is created")
#
#     # The only way to modify the instance variable value
#     # is via class methods
#     def change_password(self):
#         self.password = '1234'
#         print(self.password)
#
#
# xuv = Car()
# xuv.change_password = '345'  # this is not allowed as we're trying to modify the
#
#
# # value of the variable outside the class
#
# # Public/Private?Protected Class
#
# class MyClass:
#     def __init__(self):
#         self.name = "Himanshu"
#
#     def public_function(self):
#         print("This is a public function")
#
#     def __private_function(self):
#         print("This is a private function")
#
#     def public_fn_private(self):
#         self.__private_function()  # a private function can be accessed
#         # within the class
#
#
# obj = MyClass()
# obj.public_function()
# # obj.__private_function() # This will throw an error
# obj.public_fn_private()


# Example - Banking system

class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_number = 123456789

    def public_fn(self):
        print(self.__account_number)

    def deposit(self, amount):
        self.__balance += amount

    # ========== ENCAPSULATION - START =============

    # Encapsulation is achieved by declring he object's dta fields as private
    # and providing getters and setters methods to access and modify the data

    # Now to add encapsulation on the below method, we should make the below method as "private", so that
    # only account holder can withdraw the money
    def __withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    # same private method below
    def __show_balance(self):
        return self.__balance

    def if_you_are_auth(self, flag):
        if flag:
            return self.__show_balance()
        else:
            print("Not authorized")

    def if_you_are_auth_user(self, auth, amount):
        if auth:
            return self.__withdraw(amount=amount)
        else:
            print("Not authorized")


jp_chase = BankAccount()
# print(jp_chase.show_balance())
# jp_chase.public_fn()
jp_chase.deposit(1000)
pass_key = int(input("Enter the password: "))

if pass_key == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

pass_key = int(input("Enter the pin to withdraw: "))
your_amount = int(input("Enter the amount: "))
if pass_key == "1234":
    jp_chase.if_you_are_auth_user(True, your_amount)
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth_user(False,  your_amount)

# jp_chase.deposit(1000)
# print(jp_chase.if_you_are_auth(True))
# jp_chase.if_you_are_auth_user(True, 501)
# print(jp_chase.if_you_are_auth(True))
# ========== ENCAPSULATION - ENDS =============
