import numpy as np
# ar1=np.array([1,2,3,4,5,6])
# ar2=np.array([5,6,7,8,9,10])

# print(ar1)
ar=np.arange(9).reshape(3,3)
# print(ar)

ar1=np.arange(12,21).reshape(3,3)
# print(ar1)

print(np.concatenate((ar,ar1)))

print(np.concatenate((ar,ar1),axis=0))
print(np.concatenate((ar,ar1),axis=1))