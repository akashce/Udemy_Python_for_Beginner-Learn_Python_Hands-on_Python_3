# -*- coding: utf-8 -*-
"""
@author: Akash
Write a Python program to print the table of a number entered by the user.
"""

num = int(input("Enter the number: "))

for i in range(1,11):
    print(num,"*",i,"=",i*num)

    