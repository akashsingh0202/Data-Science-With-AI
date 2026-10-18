class Car:
    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Car({self.brand!r})"

c = Car("Honda")
print(c)