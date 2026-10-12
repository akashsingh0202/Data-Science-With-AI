# # Find the product of digits of a number.
n=int(input("enter a number :"))
total=1
while n>0:
    digit=n%10
    total=total*digit
    n=n//10

print(f"product of is : {total}")
