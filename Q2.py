"""
Q2.Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number. 
"""

def mult(value):
    unkown_number=15
    return value*unkown_number

input=int(input("Enter the to be multiply with unkown number :-"))
print(mult(input))