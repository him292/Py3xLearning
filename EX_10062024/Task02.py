# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

num = 2
sq = num ** 2
c = 8
cube = c ** 3
print(sq, cube)

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))

print(num1 if num1 > num2 else num2 if num2 > num1 else "Both numbers are equal")
print(num1 if num1 > num3 else num3 if num3 > num1 else "Both numbers are equal")
