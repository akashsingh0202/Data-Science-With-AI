import numpy as np

# 1D array
ar=np.array([3,4,5,6,78,9])
print(ar[-1])


# multi dimension array
ar1=np.array([[4,5,6],[2,3,4],[7,8,9]])

print(ar1[0][1])
print(ar1[2][2])
print(ar1[2,2])

#   fancy indexing
print(ar[[2,3,4]])
