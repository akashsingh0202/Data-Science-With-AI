import pandas as pd

s = pd.Series(
    [10, 20, 30, 40, 50],
    index=["A", "B", "C", "D", "E"]
)

print(s.loc["B":"D"])