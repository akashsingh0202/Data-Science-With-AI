def convert(i):
    c=i*2.54
    return c


i=int(input("enter a length in inches"))
print(f"the length in inches is {i} ")
print(f"the length in cm is {convert(i)}")

