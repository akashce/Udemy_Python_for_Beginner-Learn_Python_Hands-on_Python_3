"""
@author: Akash
Write a function that computes the sum of all digits.
	Pass the number as a parameter and return the computed sum.
"""

def sumofdigit(n):
    sum=0
    while(n!=0):
        number = n%10
        sum = sum + number
        n=n//10
    return sum
    
    

num = int(input("Enter the number: "))
print(sumofdigit(num))