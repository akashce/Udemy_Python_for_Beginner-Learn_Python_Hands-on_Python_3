# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:40:56 2020

@author: Akash
"""
n = int(input("Enter the number: "))

fibo = [0]*(n+1)
fibo[1]=1
sum = fibo[0] + fibo[1]
for i in range(2,n):
    fibo[i]=fibo[i-1]+fibo[i-2]
    sum = sum + fibo[i]    
print(sum)    