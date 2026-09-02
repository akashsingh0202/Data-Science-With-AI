# def add(*numbers):
#     print(numbers)

# add(10, 20, 30, 40)

def add(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(add(10, 20, 30, 40))