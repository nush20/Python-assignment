# Program to take a list of numbers and return their sum
numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
print("The sum is:", sum(numbers))
