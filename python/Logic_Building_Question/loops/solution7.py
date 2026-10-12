# 7. Calculate the factorial of a number.
# Example: 5! = 120. Assume input is a non-negative integer.

n=int(input("enter a number :"))
fact=1
for i in range (1,n+1):
    fact=fact*i
print(fact)
