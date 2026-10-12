# 6. Calculate the sum of numbers from 1 to n.
# Example: n = 5 → 1 + 2 + 3 + 4 + 5 = 15
n=int(input("enter a number :"))
sum=0
for i in range(0,n+1):
    sum=sum+i
print(sum)

