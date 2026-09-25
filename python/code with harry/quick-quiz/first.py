age=int(input("enter ur age :"))
if(age<0):
    print("Age cannot not be  negative")
elif(age>=18):
    print("You are eligible for voting")
elif(age==0):
    print("incorrect age please check once!")
elif(age<18):
    print("you are not eligible for voting")
else:
    ("you entered wrong information")