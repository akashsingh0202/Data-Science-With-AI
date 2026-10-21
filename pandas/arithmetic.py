import pandas as pd

marks = pd.Series([70, 80, 90, 60])

# print(marks.sum())
# print(marks.mean())
# print(marks.max())
# print(marks.min())


# mark = pd.Series([70, 80, None, 90])

# print(mark.count())
# print(mark.size)   # 4
# print(mark.count())  # 3

# s = pd.Series([10, 20, 30, 40, 100])

# print(s.median())

# s1 = pd.Series([10, 20, 30, 40])

# print(s1.median())


# print(marks.std())
# print(marks.var())
s = pd.Series([10, 20, 10, 30, 20, 10])

# print(s.value_counts())
print(s.nunique())
print(s.unique())
print(s.value_counts())