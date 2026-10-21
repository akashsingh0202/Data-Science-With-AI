import pandas as pd
s = pd.Series([10, 20, 10, 30, 20, 40])

print(s.duplicated().sum())
print(s.drop_duplicates().tolist())