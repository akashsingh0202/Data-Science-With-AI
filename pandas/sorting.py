import pandas as pd

# s = pd.Series([40, 10, 30, 20])

# print(s.sort_values())
# print(s.sort_values(ascending=False))


s = pd.Series(
    [40, 10, 30],
    index=["c", "a", "b"]
)

print(s.sort_index())