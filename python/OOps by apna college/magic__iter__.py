class Numbers:
    def __init__(self):
        self.data = [10, 20, 30]

    def __iter__(self):
        return iter(self.data)

n = Numbers()

for x in n:
    print(x)

class Test:
    def __iter__(self):
        return iter([5, 10, 15])

t = Test()
print(sum(t))