lines = []
while True:
    line = input("Enter a line : ")
    if line:
        lines.append(line)
    else:
        break

print("\ninpur statements:")
for line in lines:
    print(line)