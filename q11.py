 # Program to display the Fibonacci sequence up to n-th term

n = int(input("Enter n: "))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Not valid")
elif n== 1:
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1