# import numpy as num
#   # Create a program that determines whether a given year is a leap year.
#
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else :
#     print(f"{year} is not a leap year.")
#
#
# # Triangle Classifier:
#
# # Write a program that classifies a triangle based on its side lengths.
# #
# # Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
# # isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
# side_a = float(input("Enter the length of side a: "))
# side_b = float(input("Enter the length of side b: "))
# side_c = float(input("Enter the length of side c: "))
#
# if side_a == side_b and side_b == side_c:
#     print("The triangle is equilateral.")
#     # All sides are equal
# elif side_a == side_b or side_b == side_c or side_a == side_c:
#     print("The triangle is isosceles.")
#     # Exactly two sides are equal
# else:
#     print("The triangle is scalene.")
#
# # Task - Fibonacci series and Factorial
#
# # Factorial
#
# factorial = 1
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}.")
#
# # 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# # Fibonacci series
#
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
#    # On average
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
#    # Fibonnaci series upto 10:
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

# print a traingle using *
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

# write a program to find a palindrom number
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
    if temp == rev:
        print(f"{num} is a palindrome number.")
        break
        # if the number is a palindrome, break out of the loop
    else:
        print(f"{num} is not a palindrome number.")
