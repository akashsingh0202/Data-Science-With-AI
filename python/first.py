def decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))