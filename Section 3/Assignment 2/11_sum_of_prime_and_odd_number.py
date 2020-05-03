# -*- coding: utf-8 -*-
"""
@author: Akash
Write a Python program to calculate and print the sums of odd and even integers of the first n natural numbers.
"""

n = int(input("Enter the number: "))

even_total=0
odd_total=0

for i in range(1,n+1):
    if(i % 2 == 0):
        even_total = even_total + i
    else:
        odd_total = odd_total + i
    
print("The Sum of Even Numbers from 1 to ",n,"is", even_total)
print("The Sum of Odd Numbers from 1 to",n,"is", odd_total)