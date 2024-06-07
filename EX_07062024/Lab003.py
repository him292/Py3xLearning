# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# result = num1 + num2
# print(result)  # this results in STRING, as the type of vars are str


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result = num1 + num2
# print(result)
#
# # Raw string: below r is to tell the python that
# # \n is not for 'next line'
# dir = r'C:\nomedir\some dir'
# print(dir)

# format of string - can use this to format the output as per needs
first_name = "Harry"
seco_name = "Potter"
print(first_name + " " + seco_name)

print(f"{first_name} {seco_name}")  # this is the format string

# other example

b = 1
print(f"{b}x1={b}")


# List
# list is a collection of items in a particular order
# square brackets are used to define a list
# items in a list are separated by commas

# operations with list
# Add item, Remove, update, view, exit

names = ["Harry", "Ron", "Hermione"]

print(len(names))
print(names[0])
print(names[-1])

my_list = ["a", "b", "c", "d", 2, True, 3.14]
print(type(my_list))
my_list.append("ABC") # only can append one at a time : append adds item to the end of the list
print(my_list)
my_list.insert(1, "new item") # adds to a specific index


print(my_list)
my_list.remove("new item") # removes the item from the list
my_list.extend(["new1", "new2"]) # its a new list: adds multiple items to the list
print(my_list)
















