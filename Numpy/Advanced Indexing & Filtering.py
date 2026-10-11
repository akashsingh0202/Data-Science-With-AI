import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# print(arr[2])
# print(arr[[0, 2, 4]])

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[[0, 2]])
print(arr[[0, 2], [1, 2]])