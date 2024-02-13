"""
Q10.Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. Then, in another Python script, import the module and use 
the function to calculate the area of a rectangle with specific dimensions. """

import area
l=float(input("Enter the length :"))
w=float(input("Enter the length :"))
area=area.area_rectangle(l,w)
print(f"area of rectangle with length {l} and width {w} = {area}")