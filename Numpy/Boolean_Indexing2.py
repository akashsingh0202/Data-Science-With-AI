import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = arr[(arr > 20) & (arr < 60)]

print(result)

result1 = arr[(arr < 20) | (arr > 50)]

print(result1)