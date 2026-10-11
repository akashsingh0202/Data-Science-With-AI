
class Person:
    def __init__(self):
        self._name = "Akash"

p1 = Person()

print(p1._name)


class Person:
    def __init__(self):
        self._name = "Akash"


class Student(Person):
    def show(self):
        print(self._name)


s1 = Student()
s1.show()