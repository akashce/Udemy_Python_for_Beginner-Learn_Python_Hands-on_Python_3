# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:17:08 2020

@author: Akash
Write a Python program to read the three sides of a triangle and print whether the 
triangle is equilateral, isosceles or scalene.
"""
print("Program to read the three sides of a triangle and print whether the triangle is equilateral, isosceles or scalene.")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
 
if(a == b == c):
    print("As all side are of equal length it is Equilateral Triangle.")
elif(a == b or b == c or a == c ):
    print("As two side are of equal length it is Isosceles Triangle.")
else:
    print("As no side have equal lenght it is Scalene Triangle.")

