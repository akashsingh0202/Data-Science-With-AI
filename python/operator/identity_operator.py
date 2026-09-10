a = [10, 20, 30]
b = a

print(a is b)

a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)
print(a is b)

a = [10, 20]
b = [10, 20]

print(a is not b)