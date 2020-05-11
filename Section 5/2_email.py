'''
2 Write a Python program that reads the email-id of a person in the form of a string 
and ensure that it belongs to the domain @google.com.
'''
email = input("Enter E-mail id:")

domain = "@google.com"
lendo = len(domain)
lenem = len(email)
sub = email[lenem-lendo:]
if(sub == domain):
    if(lenem != lendo):
        print("It is a valid email ID")
    else : 
        print("It is an invalid email ID")  
else :  
    print("It’s domain is different")