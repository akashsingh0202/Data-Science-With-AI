class Student:
    name="akash"
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
        print("creating new student")


s1=Student("karan",99)
print(s1.name,s1.marks)
s2=Student("shyam",99)
print(s2.name,s2.marks)
        