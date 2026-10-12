# 12. Assign a grade based on marks: A (90+), B (75–89), C (60–74), D (40–59), Fail (below 40).
# Example: Marks: 82 → Grade B

n=int(input("enter a number :"))
if (n>=90):
    print("Grade : A")

elif(n>=75 and n<=89):
    print("Grade : B")

elif(n>=60 and n<=74):
    print("Grade : C")

elif(n>=40 and n<=59):
    print("Grade : D")

else:
    print("Fail")
