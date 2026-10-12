# Find the sum of digits of a number.
n=int(input("enter a number :"))
total=0
while n>0:
    digit=n%10
    total=total+digit
    n=n//10

print(f"sum of is : {total}")
