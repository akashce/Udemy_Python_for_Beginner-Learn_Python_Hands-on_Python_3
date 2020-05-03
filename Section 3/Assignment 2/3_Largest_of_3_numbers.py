'''Write a Python program to find the largest of 3 numbers.'''
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

if(num1>num2) and (num1>num3):
    largest = num1
else:
    if(num2>num3):
        largest=num2
    else:
        largest=num3

print("The Largest number is: ",largest)