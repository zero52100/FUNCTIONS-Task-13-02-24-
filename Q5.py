""""
Q5.Write a Python program to check whether a given string is a number or not using Lambda. """

to_check= lambda x: x.isdigit()


user_input = input("Enter a string: ")

if to_check(user_input):
    print(f"The user input  string : '{user_input}' is a number.")
else:
    print(f"The  user input string : '{user_input}' is not a number.")
