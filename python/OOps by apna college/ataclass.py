# from dataclasses import dataclass

# @dataclass
# class Student:
#     name: str
#     age: int

# s1 = Student("Akash", 22)

# print(s1.name)
# print(s1.age)
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

p = Product("Laptop", 50000)

print(p)