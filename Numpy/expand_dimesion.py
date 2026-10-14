import numpy as np

A = np.array([10, 20, 30])

print(A.shape)
# B = np.expand_dims(A, axis=0)

# print(B)
# print(B.shape)

C = np.expand_dims(A, axis=1)

print(C)
print(C.shape)