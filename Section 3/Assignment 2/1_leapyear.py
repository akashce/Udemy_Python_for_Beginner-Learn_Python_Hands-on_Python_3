'''1 Write a Python program to check if a year is a leap year or not'''

year = int(input("Enter the year: "))
if year % 400 == 0:
    print("It's a leap year")
else:
    if year % 4 ==0 and year % 100 !=0:
        print("It's a leap year")
    else:
        print(("Not a leap year"))
