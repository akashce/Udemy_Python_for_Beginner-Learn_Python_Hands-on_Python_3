# -*- coding: utf-8 -*-
"""
@author: Akash

Write a Python program to check if a number is divisible by another number of not
"""
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

if(num1%num2==0):
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by",num2)
