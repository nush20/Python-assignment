# Program to convert temperature from Celsius to Fahrenheit and vice versa
degree=input(" unit fahrenheit(F) or celsius(C): ")
if degree=='C':
    celsius=float(input("enter temperature in celsius: "))
    fahrenheit=(celsius*9/5)+32
    print("temperature in fahrenheit: ",fahrenheit)
elif degree=='F':
    fahrenheit=float(input("enter temperature in fahrenheit: "))
    celsius=(fahrenheit-32)*5/9
    print("temperature in celsius: ",celsius)
else:
    print("invalid unit")


    

