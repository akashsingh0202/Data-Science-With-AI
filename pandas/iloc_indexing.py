import pandas as pd

s = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)
# indexing
print(s.iloc[1])


