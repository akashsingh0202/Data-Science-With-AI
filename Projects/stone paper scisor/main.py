import random 
computer = random.choice([-1,0,1])

youstr=input("enter ur choice in stone paper scissor : in stone paper scissor ").lower()
youdict={
    "stone":-1,
    "paper":0,
    "scissor":1
}

reversedDict={
    -1:"stone",
    0:"paper",
    1:"scissor"
}

you=youdict[youstr]

print(f"you choose {reversedDict[you]} \n computer choose : {reversedDict[computer]}")
if(you==computer):
    print("its a draw :")

else:
    if(you==1 and computer==-1):
        print("sorry you loose!")

    elif(you==1 and computer==0):
        print("congracts you won!")

    elif(you==0 and computer==-1):
        print("congracts you won:")

    elif(you==0 and computer==1):
        print("sorry you loose !")

    elif(you==-1 and computer==1):
        print("congracts you won")

    elif(you==-1 and computer==0):
        print("sorry you loose")

    else:
        print("something went wrong")
