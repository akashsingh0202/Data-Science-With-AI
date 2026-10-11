import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# new_arr = arr.flatten()

# print(new_arr)
# print(arr)
# new_arr = arr.flatten()

# new_arr[0] = 100

# print(new_arr)
# print(arr)
# new_arr = arr.ravel()

# print(new_arr)
# print(arr)

# new_arr = arr.ravel()

# print(new_arr)
# print(new_arr.shape)

arr = np.array([
    [10, 20],
    [30, 40]
])

new_arr = arr.ravel()

new_arr[0] = 100

print(arr)