import pandas as pd

df=pd.read_excel("pandas/sales_dataset_50.xlsx")
# print(df)
result=df['City'].value_counts()
print(result)