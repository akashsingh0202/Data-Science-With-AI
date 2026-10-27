import pandas as pd

df=pd.read_excel("pandas/sales_dataset_50.xlsx")


# result_df=df.groupby("Category")["Quantity"].sum()
# print(result_df)
# result_df=df.groupby("Category")["Quantity"].mean()
# print(result_df)
# result_df=df.groupby("City")["Quantity"].count()
# print(result_df)


# result_df=df.groupby(["Category","City"])["Quantity"].sum()
# print(result_df)


# result_df=df.groupby("Category").agg(
#     total_quantity=('Quantity','sum'),
#     average_price=('UnitPrice','mean'),
#     # no_of_orders=('SalesID','count')
# )
# print(result_df)
# print(df.info())