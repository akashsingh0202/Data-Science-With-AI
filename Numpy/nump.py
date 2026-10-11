import numpy as np



# np.where(condition, value_if_true, value_if_false)

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr > 25)

print(result)