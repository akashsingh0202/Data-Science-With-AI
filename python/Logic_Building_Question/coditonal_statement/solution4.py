# 4. Find the greatest of three numbers.
# Example: 10, 25, 15 → 25 is greatest

num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
num3=int(input("enter a number :"))

if num1==num2==num3:
    print("all are equal")

elif(num1>num2 and num1>num3):
    print(num1)

elif(num2>num1 and num2>num3):
    print(num1)
else:
    print(num3)