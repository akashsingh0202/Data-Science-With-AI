
# single inheritance
# class Car:
#     color="white"
#     @staticmethod
#     def start():
#         print("car is started")


#     @staticmethod
#     def stop():
#         print("car is stop")

# class toyota(Car):
#     def __init__(self,name):
    
#         self.name=name

# car1=toyota("fortuner")
# car2=toyota("prius")
# print(car1.name)
# print(car1.color)
# print(car1.start())


# multilevel
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show_person(self):
#         print(f"his name is {self.name} and his age is {self.age}")

# class Student(Person):
#     def __init__(self, rollNo,name,age):
#         self.rollNo=rollNo
#         self.name=name
#         self.age=age

#     def show_student(self):
#         print(f"his roll number is {self.rollNo}")

# class CollegeStudent(Student):
#     def __init__(self, branch,rollNo,name,age):
#         self.rollNo=rollNo
#         self.name=name
#         self.age=age
#         self.branch=branch

#     def show_college_student(self):
#         print(f"and his branch is {self.branch}")


# s=CollegeStudent("Akash",22,101,"Computer Science")

# s.show_person()

# s.show_student()


# s.show_college_student()

# multipleinheritance

# class father:
#     def skill_father(self):
#         print("driving")
# class mother:
#     def skillmother(self):
#         print("cooking")
# class mine(father,mother):
#         pass


# m=mine()
# m.skill_father()
# m.skillmother()

#  heirarchical Isme ek parent ke multiple children hote hain.


# class mother:
#     def mother_skill(self):
#         print("cooking")

# class sister(mother):
#     def sister_skill(self):
#         print("dancing")


# class me(mother):
#     def mine_skill(self):
#         ("cricket")
# s=sister()
# m = me()

# s.mother_skill()
# s.sister_skill()

# m.mother_skill()
# m.mine_skill()



# hybrid 
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


class Puppy(Dog, Cat):

    def play(self):
        print("Puppy is playing")
        

p = Puppy()
p.eat()
p.bark()
p.meow()
p.play()
     