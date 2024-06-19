# # numbers = [1, 2, 3]
# #
# #
# # #collection of items
# #
# # def do_something(test_list):
# #     test_list.append(4)
# #     test_list[0] = 100
# #     print(test_list)
# #
# #
# # numbers.append(10)
# # do_something(numbers)
#
# # Important question
# # Lambda expression - to do a task in one line
#
# def sum_two(a,b):
#     return a + b
#
# o_f = lambda a,b:a+b # instead of above function use one liner lamba
# print(o_f(1,2))
#
# # But Lambda is not recommended for complex functions
# # use def instead of lambda for complex function
#
# # take inputs using Lambda
#
# # power number
# sq_number = lambda : int(input("Enter a number: "))**2
# result = sq_number()
#
# print(result)

# double the numbers within the list

# list = [1, 4, 5, 7]
# temp_list = []
#
# for item in list: # here item is used to take each item from the list
#     temp_list.append(item * 2)
#
# print(temp_list)

# OR - double the list using Map()
my_list = [1, 4, 5, 7]

def double_item(num):
    return num * 2


# Map()
# Takes each item from list
# execute function on it
# return same no of elements (list)
# return modified list

double_list = list(map(double_item, my_list))
print(double_list)

# Tuple

my_list = [1,2,3,4,5]
print(my_list)
my_list[0] = 21
print(my_list)
print(id(my_list))

my_tuple = (1, 2,3,4,5)
print(my_tuple)

