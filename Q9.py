""""
Q9.Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list: 

['Python', 3, 2, 4, 5, 'version'] """


original_list = ['Python', 3, 2, 4, 5, 'version']
num=filter(lambda x: isinstance(x, (int, float)), original_list)
print("Maximum value in the list:", max(num))

