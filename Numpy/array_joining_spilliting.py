import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])

# result = np.concatenate((a, b))

# print(result)

# a = np.array([[1, 2],
#               [3, 4]])

# b = np.array([[5, 6],
#               [7, 8]])

# print(np.concatenate((a, b), axis=1))

# arr = np.array([10, 20, 30, 40, 50, 60])

# result = np.split(arr, 3)

# print(result)



a = np.array([[1, 2]])
b = np.array([[3, 4]])

print(np.concatenate((a, b), axis=0))