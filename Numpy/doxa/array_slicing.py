import numpy as np

# 1D array
ar=np.array([3,4,5,6,78,9])
print(ar[1:5:2])


# multi dimension array
ar1=np.array([[4,5,6],[2,3,4],[7,8,9]])

# print(ar1[0][1])
# print(ar1[2][2])
# print(ar1[2,2])
print(ar1[0:2, 1:3])
# print(ar1[0:2, 0:2])