import numpy as np

# print(ar1)
ar=np.arange(9).reshape(3,3)
# print(ar)

ar1=np.arange(12,21).reshape(3,3)
# print(ar1)

# hstack by works on axis =1

print(np.hstack([ar,ar1]))  

# vstack by works on axis =0

print(np.vstack([ar,ar1])) 