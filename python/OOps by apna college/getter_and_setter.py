#  Getter = private variable ki value read/get karna.

class Person:
    def __init__(self):
        self.__name = "Akash"

    def get_name(self):
        return self.__name

p1 = Person()

print(p1.get_name())

# Setter = private variable ki value change/set karna.
class Person:
    def __init__(self):
        self.__name = "Akash"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


p1 = Person()

print(p1.get_name())

p1.set_name("Rahul")

print(p1.get_name())



# Getter + Setter

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")


e1 = Employee(50000)

print(e1.get_salary())

e1.set_salary(-1000)

print(e1.get_salary())