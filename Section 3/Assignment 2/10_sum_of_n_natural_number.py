# -*- coding: utf-8 -*-
"""
@author: Akash
Write a Python program to print the sum of first n natural numbers, where n is entered by the user.
"""
n = int(input("Enter the number: "))
num = n
a=0
for i in range(num):
    a=a+num
    num=num-1

print("The sum of first",n,"natural number is ",a)