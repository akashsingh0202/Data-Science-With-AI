def sums(n):
    sum=0
    for i in range (1,n+1):
        sum=sum+i
    return sum

n=int(input("enter a number :  "))
print(f"sum = {sums(n)}")