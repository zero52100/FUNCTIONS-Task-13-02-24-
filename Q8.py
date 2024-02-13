"""
Q8.Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results. 

Original list: [2, 4, 6, 9, 11] 

Given number: 2 

Result: 

4 8 12 18 22 """


numbers = [2, 4, 6, 9, 11] 
Given_number=int(input("Entnr the number to multiplies with the list"))
result = list(map(lambda x: x * Given_number, numbers))
print("Results after multiplying each number ", result)
