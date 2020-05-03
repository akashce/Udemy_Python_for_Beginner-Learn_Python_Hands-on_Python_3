# -*- coding: utf-8 -*-
"""
@author: Akash
Write a Python program to print the following pattern:

Example: n=5

* * * * *
* * * *
* * *
* *
*
"""

num = int(input("Enter the number: "))

for i in range(num,0,-1):
    for j in range(0,i):
        print(" * ",end=" ")   
    print("  ")
