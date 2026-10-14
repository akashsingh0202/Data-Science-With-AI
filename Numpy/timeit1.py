import timeit

numbers = list(range(1000))

python_time = timeit.timeit(
    "[x * 2 for x in numbers]",
    globals=globals(),
    number=100
)

print(python_time)