# class School:
#     school_name="HGV"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


# s=School("akash",22)
# print(s.school_name,s.name,s.age)
        

class Student :
    def __init__(self,name , marks):
        self.name=name
        self.marks=marks

    def getAvg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your pecentage is ",sum/3)




s1=Student("tony",[100,98,99])
s1.getAvg()
        