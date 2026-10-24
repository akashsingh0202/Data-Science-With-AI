import pandas as pd

df=pd.read_excel("pandas/sales_dataset_50.xlsx")
# print(df)
# print(df.dtypes)
# print(df["Quantity"].dtype)
# print(df["Revenue"].dtype)
# print(df["SalesDate"].dtype)
# df["Quantity"] = df["Quantity"].astype(float)
# print(df["Quantity"].dtype)
# df["SalesDate"] = pd.to_datetime(df["SalesDate"])
# df["Revenue"] = pd.to_numeric(df["Revenue"])
# print(df.dtypes)

# df["Revenue"] = pd.to_numeric(
#     df["Revenue"],
#     errors="coerce"
# )

# print(df["Revenue"].dtype)
# print(df["Revenue"].isna().sum())
# print(df["SalesDate"].head(10).to_list())
# print(df["SalesDate"].dtype)

df["SalesDate"] = pd.to_datetime(
    df["SalesDate"],
    format="%Y-%m-%d"
)

print(df["SalesDate"].dtype)


print(df["Quantity"].dtype)
print(df["Revenue"].dtype)
print(df["SalesDate"].dtype)