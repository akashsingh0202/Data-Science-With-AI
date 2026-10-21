import pandas as pd

s = pd.Series([10, 20, None, 40, None])

# print(s)
# print(s.isna())
# print(s.isna().sum())
# print(s.fillna(0))
# print(s.fillna(s.mean()))
print(s.dropna().mean())