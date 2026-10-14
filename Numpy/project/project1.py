import numpy as np

marks = np.array([45, 78, 90, 56, 88, 32, 67, 95, 49, 81])
print(marks)
print(marks.shape)
print(marks.size)
print(marks.ndim)
print(marks>60)
print(marks[marks>60])
print(np.max(marks))
print(np.min(marks))
print(np.mean(marks))
print(np.argmax(marks))
print(np.argmin(marks))
print(np.sum(marks >= 70))
print(np.sort(marks))
print(np.split(marks,2))
print(marks[(marks > 70) & (marks < 90)])

