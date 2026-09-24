def greatest(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c

a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))

print(f"the greatest number is { greatest(a,b,c)}")