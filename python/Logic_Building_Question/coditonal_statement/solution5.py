# 5. Check whether a person is eligible to vote (age ≥ 18).
# Example: Age: 20 → Eligible

n=int(input("enter ur age :"))

if n<0:
    print("age can't be negative")

elif(n>=18):
    print("you can vote ")

else:
    print("you are not eligible for vote")