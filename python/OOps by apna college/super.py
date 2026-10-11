class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person(self):
        print(f"his name is {self.name} and his age is {self.age}")

class Student(Person):
    def __init__(self, rollNo,name,age):
        super().__init__(name,age)
        self.age=age

    def show_student(self):
        print(f"his roll number is {self.rollNo}")

class CollegeStudent(Student):
    def __init__(self, branch,rollNo,name,age):
        super.__init__(name,age,rollNo)
        self.branch=branch

    def show_college_student(self):
        print(f"and his branch is {self.branch}")


s=CollegeStudent("Akash",22,101,"Computer Science")

s.show_person()

s.show_student()


s.show_college_student()