import pandas as pd

# s = pd.Series([10, 20, 30])

# print(s.apply(lambda x: x * 2))
# print(s.apply(lambda x: x + 3))

s = pd.Series([2, 4, 6])

print(s.map({2: "Two", 4: "Four", 6: "Six"}))