import numpy as np

# # arr = np.array([10, 20, 30, 40],dtype=np.int32)
# arr = np.array([10, 20, 30], dtype=float)

# print(arr)
# arr1 = np.array([10.5, 20.5], dtype=np.float32)

# arr2 = np.array([10.5, 20.5], dtype=np.float64)

# print(arr.dtype)
# print(arr1.dtype)
# print(arr2.dtype)
# print(type(arr))

arr=np.array([10,20,30])

new_arr=arr.astype(float)

print(new_arr)
print(new_arr.dtype)
