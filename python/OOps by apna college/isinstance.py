# isinstance() — check karta hai ki object kisi class ka instance hai ya nahi.
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))
print(isinstance(d, Animal))