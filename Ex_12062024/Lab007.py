# multiple condition - practice debugging
# def check_conditions(n):
#     if n % 2 == 0:
#         print("n is even")
#     if n % 3 == 0:
#         print("n is divisible by 3")
#     if n % 4 == 0:
#         print("n is divisible by 4")

# a = 10
# b = 45
# x = 10
# y = 67
#
# result1 = (a > b)
# result2 = (x < y)
# result3 = result1 and result2
# print(result3)

# program to find max between 3 numbers

# a = int(input("Enter your first num: "))
# b = int(input("Enter your second num: "))
# c = int(input("Enter your third num: "))
#
#
# def max_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

#
# print("maximum out of three numbers is :", max_of_three(a, b, c))

# Loops code - repeat a block of code multiple times

i = 0
while i < 5:
    print(i)
    i = i + 1
