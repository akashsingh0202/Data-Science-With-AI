import numpy as np

arr = np.array([10, 20, 30])

view_arr = arr.view()
copy_arr = arr.copy()

view_arr[0] = 99

print(arr)
print(copy_arr)
