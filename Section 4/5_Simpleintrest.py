'''
Write a function that computes the simple interest.
	Pass the principal amount, the rate and the time as parameters to the function.
'''
def simpleIntrest(p,r,t):
    simpleintrest = (p * r *t)/100
    return simpleintrest


principleamount = float(input("Enter the Principal Amount in Rs: "))
rate_of_intrest = float(input("Enter the Rate of Interest: "))
Time_period = float(input("Enter the time period in Years: "))
print(simpleIntrest(principleamount,rate_of_intrest,Time_period))
