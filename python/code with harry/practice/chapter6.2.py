marks1=int(input("enter first sub marks"))
marks2=int(input("enter second sub marks"))
marks3=int(input("enter third sub marks"))

percentage=(marks1+marks2+marks3)/3

if(percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("congracts you are pass")
else:
    print("sorry you are fail better luck next time!")