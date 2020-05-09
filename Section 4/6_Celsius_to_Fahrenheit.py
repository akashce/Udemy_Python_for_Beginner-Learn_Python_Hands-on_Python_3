'''
Write a function that converts Celsius reading to Fahrenheit reading.
	Read the Celsius value from the user in the function and also print the Fahrenheit reading in the function itself.
'''
def toFahrenheit():
    celsius = float(input("Enter the Celsius value: "))

    Fahrenheit = (9/5)*celsius + 32
    print("{0:.2f}".format(Fahrenheit))

toFahrenheit()