def  convert(c):
    f=(c*9/5)+32
    return f


c=int(input("enter a temperature in celcius : "))
print(f"the temperature in celcius is {c}")
print(f"the temperature in fahrenheit is{convert(c)}")