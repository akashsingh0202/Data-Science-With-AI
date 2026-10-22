import pandas as pd

df = pd.read_excel("sales_dataset_50.xlsx")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.sample())
# df.info()
print(df.describe())
print(df.describe(include="all"))