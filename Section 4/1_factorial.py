# -*- coding: utf-8 -*-
"""
@author: Akash
    Write a function that computes the factorial of a number.
	The function should take the number as a parameter and return the factorial value.
    
"""
def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    print(factorial)
    return factorial


n = int(input("Enter the number of which you want factorial: "))
if(n<0):
    print("Enter positive number!")
elif(n==0):
    print("Factorial of 0 is 0")
else:
    fact(n)


    