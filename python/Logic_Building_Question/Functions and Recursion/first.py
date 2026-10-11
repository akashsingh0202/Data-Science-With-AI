a=int(input("enter a number :"))
b=int(input("enter a number :"))

def sum(a,b):
    while b!=0:
        carry=a&b
        a=a^b
        b=carry<<1

    return a
print(sum(a,b))
    