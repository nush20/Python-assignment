 # Program to calculate the sum of the digits of a given number
num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num)
print("The sum of the digits is:", digit_sum)
