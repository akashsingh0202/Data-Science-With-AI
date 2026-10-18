class Teacher:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, teacher):
        self.teacher = teacher

t1 = Teacher("Rahul")
s1 = School(t1)

print(s1.teacher.name)