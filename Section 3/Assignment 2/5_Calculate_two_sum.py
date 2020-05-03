# -*- coding: utf-8 -*-
"""
@author: Akash

5_Write a Python program that inputs three numbers and calculates two sums as per this:
a)Sum 1 as the sum of all numbers.
b)Sum 2 as the sum of non-duplicate numbers, if there are duplicates, then ignore them.
"""

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

sum1 = num1 + num2+ num3
print("The sum of all three numbers is ",sum1)

if(num1!=num2) and (num2!=num3) and (num1!=num3):
    print("Sum of three number is  ",num1+num2+num3)
else:
    if(num1==num2) and (num2==num3):
        print("Sum is 0 as all number are same")
    elif(num1==num2):
        print("Sum after ignoring the duplicate number is ",num3)
    elif(num1==num3):
        print("Sum after ignoring the duplicate number is ",num2)
    else:
        print("Sum after ignoring the duplicate number is ",num1)
