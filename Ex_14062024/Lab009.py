num = int(input("enter a number: "))

res = 1

printMultiplication = ""

for i in range(num, 0, -1):
    res = num * res

    printMultiplication += str(i) + "*"

print(printMultiplication)

print("Factorial of a num :", res)
