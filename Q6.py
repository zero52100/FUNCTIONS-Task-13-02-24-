""""
Write a Python program to create Fibonacci series up to n using Lambda. 

Fibonacci series upto 2: 
[0, 1] 
Fibonacci series upto 5: 
[0, 1, 1, 2, 3] 
Fibonacci series upto 6: 
[0, 1, 1, 2, 3, 5] """
fib = lambda n: [0] if n == 0 else [0, 1] if n == 1 else fib(n - 1) + [fib(n - 1)[-1] + fib(n - 2)[-1]]

n = int(input("Enter the value: "))

series = fib(n)

print(f"Fibonacci series up to {n}: {series}")



