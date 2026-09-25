import random

computer=random.choice([-1,0,1])
youstr=input("Enter ur choice : ").lower()
youDict={"s":-1,"w":0,"g":1}
reverseDict={-1:"Snake",0:"Water",1:"Gun"}
you=youDict[youstr]
print(f"you choose {reverseDict[you]} \n computer choose {reverseDict[computer]}")


if (computer==you):
    print("It's a draw")

else:
    if(computer==-1 and you==1):
        print("congracts! you won ")

    elif(computer==-1 and you==0):
        print("sorry you loose!")

    elif(computer==1 and you==-1):
        print("Sorry you loose")

    elif(computer==1 and you==0):
        print("congracts you won")

    elif(computer==0 and you==-1):
        print("you loose")

    elif(computer==0 and you==1):
        print("congracts ! you won ")

    else:
        print("something went wrong??")