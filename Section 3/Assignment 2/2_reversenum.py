'''2 Write a Python program to read a number from the user and print the reversed number.'''

num1 = int(input("Enter the number: "))
rev = 0

while(num1>0):
    a = num1 % 10
    rev = rev * 10 + a
    num1 = num1//10
    
print(rev)
    