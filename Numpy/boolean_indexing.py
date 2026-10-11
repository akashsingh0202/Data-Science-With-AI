import numpy as np
#  1D array
# a = np.array([10, 20, 30, 40, 50],60)

# print(a > 25)
# print(a[a > 25])

# a[(a > 20) & (a < 50)]


#  2D array
b = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# print(b[b > 50])
# print(print(b[b == 50]))

# print(b[(b > 20) & (b < 80)])


c = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print(c[c > 70])
print(c[(c >= 30) & (c <= 90)])
print(c[c % 20 == 0])