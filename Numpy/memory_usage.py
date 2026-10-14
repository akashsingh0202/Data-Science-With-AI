import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr.dtype)
print(arr.nbytes)

arr = np.array([2, 4, 6], dtype=np.int32)

print(arr.nbytes)