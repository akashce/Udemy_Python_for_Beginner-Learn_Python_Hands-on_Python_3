# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:32:26 2020

@author: Akash
Write a  Python program to print the second largest number from 3 numbers entered by the user.
"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if(a==b and b==c):
    print("All number are equal.")
elif(a<b and b<c):
    print(b," is Second largest number.")
elif(b<a and a<c):
    print(a," is Second largest number.")
else:
    print(c,"is Second largest number.")