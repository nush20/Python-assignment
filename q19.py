# Program to remove all punctuation from a given string
import string

input_str = input("Enter a string: ")
output_str = input_str.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", output_str)
