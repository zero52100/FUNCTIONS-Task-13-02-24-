"""
Q3.Write a Python program to find if a given string starts with a given character using Lambda. """




check = lambda string, value: string.startswith(value)


inputstring= input("Enter a string: ")
value = input("Enter the character to check for: ")
result = check(inputstring, value)
if result:
    print(f"The input string starts with '{value}'.")
else:
    print(f"The input string doesn't start with  '{value}'.")
