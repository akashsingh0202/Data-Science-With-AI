import numpy as np
ar1=np.array([1,2,3,4])
ar2=np.array([5,6,7,8])


# 1D array
# print(np.sum(ar1))

ar2=np.array([[5,6,7,8],[3,4,5,6],[6,7,8,9]])

# print(np.sum(ar2))
# print(np.sum(ar2,axis=0))
# print(np.sum(ar2,axis=1))

# print(np.mean(ar2))
# print(np.mean(ar2, axis=0))
# print(np.mean(ar2, axis=1))

# print(np.median(ar2))
# print(np.median(ar2, axis=0))
# print(np.median(ar2, axis=1))

# print(np.max(ar2))
# print(np.max(ar2,axis=0))
# print(np.max(ar2,axis=1))

# print(np.min(ar2))
# print(np.min(ar2,axis=0))
# print(np.min(ar2,axis=1))


# print(np.var(ar2))
# print(np.var(ar2,axis=0)) 
# print(np.var(ar2,axis=1)) 


# print(np.std(ar2))
# print(np.std(ar2,axis=0))
# print(np.std(ar2,axis=1))

# print(np.argmin(ar2))
# print(np.argmin(ar2,axis=0))
# print(np.argmin(ar2,axis=1))


# print(np.argmax(ar2))
# print(np.argmax(ar2,axis=0))
# print(np.argmax(ar2,axis=1))


print(np.percentile(ar2,50))
print(np.percentile(ar2,50,axis=0))
print(np.percentile(ar2,50,axis=1))




