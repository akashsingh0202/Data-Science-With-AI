# Check whether a number is an Armstrong number.


n = int(input("Enter a number: "))
original = n
total = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
