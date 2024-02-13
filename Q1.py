"""
Q1.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and prints the result. 
"""

add=lambda x:x+15
mult=lambda x,y:x*y
value1=float(input("Enter the value 1:"))
value2=float(input("Enter the value 2:"))
print(f"{value1} + 15 = {add(value1)}")
print(f"{value1} * {value2} = {mult(value1,value2)}")


