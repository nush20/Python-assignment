# Program to count the frequency of each character in a string
str = input("Enter a string: ")
frequency = {}
for char in str:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequencies:")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")
