# 5. Write a Class ‘Train’ which has methods
#  to book a ticket, get status (no of seats) and 
# get fare 
# information of train running under Indian Railways.



from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def bookTicket(self,fro,to):
        self.fro=fro
        self.to=to
        print(f"ticket is booked in {self.trainNo} from {fro} to {to}")




    def getStatus(self):
        print(f"{self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"ticket is booked in {self.trainNo} from {fro} to {to} is {randint(222,5555)}")


t=Train(123999)
t.bookTicket("rampur","delhi")
t.getStatus()
t.getFare("rampur","delhi")