# Program to copy the contents of one text file to another
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

with open(source_file, "r") as src:
    content = src.read()

with open(destination_file, "w") as dest:
    dest.write(content)

print(f"Contents copied from {source_file} to {destination_file}")
