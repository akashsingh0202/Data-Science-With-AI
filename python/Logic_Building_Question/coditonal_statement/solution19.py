# 19. Calculate the absolute value of a number without using abs().
# Example: Number: -12 → 12
n = int(input("Enter a number: "))

if n < 0:
    n = n * -1

print(n)