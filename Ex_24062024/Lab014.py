# Recursion
# recursion is a technique where a function calls itself to solve a problem

# take example of factorial
def recursion(n):
    # base case
    if n == 0 or n == 1:
        return 1
    else:
        # recursive case
        return n * recursion(n-1) # this recursive case will run until it reaches the base case

# this function calls itself

print(recursion(5))  # 120


# LeetCode - Sum of digits ( 1 + 2 + 3 + 4 + 5)

number = 12345
remainder = number % 10
quotient = number // 10
print(remainder)  # 5
print(quotient)  # 1234

remainder2 = quotient % 10
quotient2 = quotient // 10
print(remainder2)  # 4
print(quotient2)  # 123

remainder3 = quotient2 % 10
quotient3 = quotient2 // 10
print(remainder3)  # 3
print(quotient3)  # 12

remainder4 = quotient3 % 10
quotient4 = quotient3 // 10
print(remainder4)  # 2
print(quotient4)  # 1

remainder5 = quotient4 % 10
quotient5 = quotient4 // 10
print(remainder5)  # 1
print(quotient5)  # 0

sum_of_digits = remainder + remainder2 + remainder3 + remainder4 + remainder5
print(sum_of_digits)

# now to convert the above code in to recursive function
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))  # 15

#   OR  (without using recursion)

def sum_of_digits2(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


print(sum_of_digits2(12345))  # 15