
import numpy as np

# 1D array
a = np.array([10, 20, 30, 40, 50])
print(a[2])
# negative indexing
print(a[-1])

# 2D array
b = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(b[2, 0])

print(b[0, :])