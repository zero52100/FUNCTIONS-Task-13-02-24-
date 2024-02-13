"""
Q7.Write a Python program to find palindromes in a given list of strings using Lambda. """


is_palindrome = lambda s: s == s[::-1]
strings_list = ["roor", "top", "malayalam"]
palindromes = list(filter(is_palindrome, strings_list))
print(f"Palindromes : {palindromes}")

