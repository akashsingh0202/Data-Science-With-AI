#  1D array
import numpy as np

# arr = np.array([10, 20, 30, 40,50,60])

# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# new_arr1 = arr.reshape(2, 3)
# print(new_arr1)




# 2D Array
# arr1 = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# new_arr2 = arr.reshape(3,2)
# print(new_arr2)

arr = np.arange(1, 13)
# NumPy mein -1 ka matlab hota hai NumPy khud us dimension ko calculate karega
print(arr.reshape(3, -1))