import numpy as np
#  RULES
# 1 where your having lowest dimension
   # add 1 at its head position
   #why? to make sure both are having  same dimesion

# 2 after making both as same dim drag value of 1 to its respected value position
# 
# violation : if shapes are mis matching , if there is no 1 to drag then 
# broadcasting is not possible   
# arr = np.array([10, 20, 30])

# print(arr + 5)


# ar1=np.arange(15).reshape(3,5)

# ar2=np.arange(5).reshape(1,5)

# print(ar1*ar2)

ar1=np.arange(15).reshape(3,5)

ar2=np.arange(5).reshape(1,5)

print(ar1*ar2)

