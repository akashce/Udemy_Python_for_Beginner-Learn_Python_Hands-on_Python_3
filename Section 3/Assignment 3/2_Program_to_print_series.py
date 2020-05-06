# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:34:59 2020
.
@author: Akash
Write a Python program to print the following series:
	a) 1,4,7,10….n terms
	b) 1,-4,7,-10,…,n terms
"""
print("Program to print series")
print("Which series you want to print")
print("Press 0 for the series 1,4,7,10,...,n or Press 1 for the series 1,-4,7,-10,...,n ")
choice = int(input("Enter choice: "))

n = int(input("Enter the last number of series: "))
a = 1
if(choice == 0):
    while(a < n+1):
        print(a,end=",")
        a=a+3
else:
    while(a<n+1):
        if(a%2==0):
            print(-a,end=",")
            a=a+3
        else:
            print(a,end=",")
            a=a+3
    
    

    

