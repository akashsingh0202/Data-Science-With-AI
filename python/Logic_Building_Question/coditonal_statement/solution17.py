# 17. Check whether a number is a two-digit number.
# Example: Number: 45 → Two-digit

n=int(input("enter a number :"))
if n<9:
    print("single digit")

elif(n>9 and n<99):
    print("Double digit")

else:
    print("Multiple Digit")