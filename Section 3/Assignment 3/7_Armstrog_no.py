# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:30:23 2020

@author: Akash
Write a Python program to check if a number is an Armstrong number or not.
"""

n = int(input("Enter the number to check: "))
sum = 0
temp =n

while(temp>0):
    digit = temp % 10
    sum = sum + (digit**3)
    temp = temp//10

if(n==sum):
    print("Sum is ",sum,".So,",n," is Armstrong Number.")
else:
    print(n," is not Armstrong number.")