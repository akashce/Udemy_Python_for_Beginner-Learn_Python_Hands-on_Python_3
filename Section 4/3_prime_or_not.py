'''
Write a function that checks if a number is prime or not.
Pass the number as a parameter and return True if the number is prime, otherwise return False.
'''

def isprime(num):
    for i in range(2,num):    
        if(num % i==0):
            return("is_not_prime")
    else:
        return ("is_prime")


num = int(input("Entet the number to check: "))
print(isprime(num))