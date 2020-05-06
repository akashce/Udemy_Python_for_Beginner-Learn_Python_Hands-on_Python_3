# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:13:46 2020

@author: Akash
Write a Python program to print the following pattern:
	Example: n=3

	*

	*  *

	*  *  *

	*  *

	*
"""
n = int(input("Enter the number: "))

for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print(" ")
    
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print(" ")
