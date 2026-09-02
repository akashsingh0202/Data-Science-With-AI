# def outer(x):

#     def inner():
#         return x + 10

#     return inner

# result = outer(20)

# print(result())

def multiplier(x):

    def multiply(number):
        return number * x

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))