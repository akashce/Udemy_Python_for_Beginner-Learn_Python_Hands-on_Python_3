# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:16:03 2020

@author: Akash
Write a Python program to check if the square of a number is prime or not.
"""
print("Program to check if the square of a number is prime or not.")

num = int(input("Enter the number: "))
sqr=num**2

if(sqr > 1):
    for i in range(2,sqr):
        if(sqr % i == 0):
            print(sqr," is not prime number.")
            print(i," times ",sqr//i," is ",sqr)
            break
    else:
        print(sqr,"is prime number.")
else:
    print(num,"is not a prime no.")