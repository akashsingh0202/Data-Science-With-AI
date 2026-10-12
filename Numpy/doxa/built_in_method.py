import numpy as np

#  build in method of creation of arrays
# properties

# ar1=np.array([[1,2,3,4,5],[1,9,8,7,6]])
# print(ar1.shape)
# print(ar1.ndim)
# print(ar1.size)

# ar2=np.array([[[[[1,2,3,4,5],[1,9,8,7,6]]]]])
# print(ar2.ndim)
# print(ar2.shape)



#  zeroes
# ar3=np.zeros((2,3))
# print(ar3)

# ones
# ar4=np.ones((2,3))
# print(ar4)

# ar5=np.identity((5))
# print(ar5)

# ar5=np.eye((5))
# print(ar5)


# ar6=np.diag([3,4,5,6,7])
# print(ar6)


# ar7=np.array([[1,2,3,4],[5,6,7,8],[8,9,2,3],[4,3,2,1]])
# print(ar7)
# print(ar7.T)

# iterate

ar8=np.array([[1,2,3,4],[5,6,7,8]])
# flatten is a copy
# print(ar8.flatten())

# ravel is view
print(ar8.ravel())



