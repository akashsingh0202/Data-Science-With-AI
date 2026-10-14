import numpy as np
import timeit

numbers = list(range(1000))
arr = np.array(numbers)

print("timeit module:", timeit.__file__)

python_time = timeit.timeit(
    "[x * 2 for x in numbers]",
    globals=globals(),
    number=100
)

numpy_time = timeit.timeit(
    "arr * 2",
    globals=globals(),
    number=100
)

print("Python loop:", python_time)
print("NumPy:", numpy_time)