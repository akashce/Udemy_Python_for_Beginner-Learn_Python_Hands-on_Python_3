'''
Write a Python program that checks if a string is a palindrome or not.
'''
str = input("Enter the string to check: ")
rev_str = reversed(str)

if(list(str) == list(rev_str)):
    print("Palindrome")
else:
    print("Not palindrome")