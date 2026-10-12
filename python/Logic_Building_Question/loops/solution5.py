# 5. Print the multiplication table of a number entered by the user.
# Example: input 5 → 5 × 1 through 5 × 10.
n=int(input("enter a number :"))
for i in range(1,11):
    print(f"{n}  X  {i} = {n*i}")