# # Ques no.=1
# Student naam ki class banao. Usme:

# name
# age

# properties rakho.

# Ek object banao aur dono values print karo.

# # ans no.=1
# class Student:
#     name="akash"
#     age=23

# s=Student()
# print(s.name,s.age)


# Q2. Car class banao jisme:

# brand
# color
# price

# ho.

# Ek object create karke values print karo.
# # ans no 2
# class Car:
#     brand="mercedes"
#     color="red"
#     price=10000000

# c=Car()
# print(c.brand,c.color,c.price)

# Q3. Employee class banao jisme:

# name
# salary

# ho.

# 2 objects banao:

# # ans=3
# class Employee:
#     name="akash"
#     salary=120000

# e=Employee()
# print(e.name,e.salary)

# Q4. Student class banao aur __init__() constructor ka use karo.

# # ans=4
# class Students:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# s1=Students("akash",22)
# print(s1.name,s1.age)

# Q5. Mobile class banao.

# Constructor mein:

# brand
# model
# price

# receive karo.

# ans=5
# class Mobile:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price

# m=Mobile("samsung","S24",70000)


# Q6. Ye program khud likho:

# Class: Employee

# Constructor:
# name
# salary
# department

# Method:
# display()
#  ans=6

class Employee:
    def __init__(self ,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def display(self):
        print("name :" ,self.name)
        print("salary :" ,self.salary)
        print("department :" ,self.department)

e1=Employee("akash",120000,"IT")
e1.display


# Q7. Rectangle class banao.

# Constructor mein:

# length
# width
# ans =7
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        


    def area(self):
        area=self.length*self.breadth
        print("Length of rectangle is :",self.length)
        print("breadth of rectangle is :",self.breadth)
        print("area of rectangle is : ",area)

        
r=Rectangle(10,5)
r.area()


# Q8. BankAccount class banao.

# Constructor mein:

# name
# balance

# lo.

# Do methods banao:

# deposit(amount)
# withdraw(amount)
#  ans =8
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,deposit):
        self.balance+=deposit
        print("Updated balance",self.balance)

    
    def withdraw(self,withdraw):
        self.balance-=withdraw
        print("Updated balance",self.balance)

b=Bank("akash",100000)
b.withdraw(10000)
b.deposit(3000)

# Q9. Car class banao.

# Constructor:

# brand
# speed

# Method:

# accelerate()

# Har baar speed mein 10 add ho.
# ans=09

class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def accelerate(self):
        self.speed+=10
        print("now the speed is ", self.speed)
        
c=Car("Mercedes",100)
c.accelerate()
c.accelerate()


