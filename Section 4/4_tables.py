'''
Write a function that prints the table of a number.
Pass the number as a parameter to the function.
'''
def table(n):
    for i in range(1,11):
        print(n," x ",i," = ",n*i)


num = int(input("Enter the number: "))
table(num)
