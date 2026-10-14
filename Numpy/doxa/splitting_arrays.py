import numpy as np
ar=np.arange(9).reshape(3,3)
print(ar)

print(np.hsplit(ar,3))  #axis=0
print(np.vsplit(ar,3)) #axis=1



