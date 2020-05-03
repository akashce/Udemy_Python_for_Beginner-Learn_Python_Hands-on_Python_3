# -*- coding: utf-8 -*-
"""
@author: Akash

Write a Python program to read three numbers and print them in ascending order
"""
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

a1 = min(num1,num2,num3)
a3 = max(num1,num2,num3)
a2 = (num1+num2+num3)-a1-a3

print("The Ascending order is: ",a1,a2,a3)