'''
Design a function having parameters and no return statement
'''

def oddnumber(n):
    for i in range(1,n+1):
        if(i%2!=0):
            print(i)

num = int(input("Enter the number of the odd number: "))
oddnumber(num)