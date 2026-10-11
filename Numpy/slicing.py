import numpy as np


# #  1D array
# a = np.array([10, 20, 30, 40, 50])


# print(a[1:])
# print(a[1:4])
# print(a[:4])
# print(a[:])

# print(a[0:5:2])

# print(a[::-1])


# b = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# # b[row_start:row_stop, column_start:column_stop]

# print(b[2:3, :])

# print(b[:, 0:2])

b = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# print(b[0:2, :])
# print(b[:, 1:3])
# print(b[1:, 2:])
print(b[::-1])