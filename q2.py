 # Program to calculate the factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("The factorial is:", factorial(num)) 