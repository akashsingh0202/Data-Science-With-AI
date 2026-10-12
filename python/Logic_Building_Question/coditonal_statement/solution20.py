# 20. Check whether a student passes or fails in three subjects (pass mark 33 in each).
# Example: Marks: 50, 60, 20 → Fail

marks1=int(input("enter first subject marks :"))
marks2=int(input("enter second subject marks :"))
marks3=int(input("enter third subject marks :"))

if (marks1>33 and marks2>33 and marks3>33):
    print("pass")

else:
    print("fail")