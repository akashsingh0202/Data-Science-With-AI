# class Calculator:

#     @staticmethod
#     def add(a, b):
#         print("sum is ",a+b)

# Calculator.add(10, 20)


# class Maths:
#     @staticmethod
#     def square(n):
#         print("the square is :",n*n)

# Maths.square(5)


# class Number:
#     @staticmethod
#     def check_even(n):
#         if(n%2==0):
#             print("number is even : ",n)

#         else:
#             print("number is odd : ",n)

# Number.check_even(5)

# class Calculator:

#     @staticmethod
#     def multiply(a, b):
#         print("multiply is ",a*b)

# Calculator.multiply(10, 20)


# class Employee:
#     company="TCS"
#     @staticmethod
#     def showCompany():
#         print("the company is",Employee.company)
# e=Employee
# e.showCompany()


class Student:
    school="HGV"
    @staticmethod
    def isAdult(age):
        if(age>=18):
            print("adult")
        else:
            print("minor")
Student.isAdult(20)
    