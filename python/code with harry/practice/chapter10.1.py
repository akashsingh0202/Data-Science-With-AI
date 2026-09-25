# Create a class “Programmer”
#  for storing information of
#  few programmers working at Microsoft. 

class Programmer :
    company="Microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("harry",12000,233)
print(p.name,p.salary,p.company,p.pin)