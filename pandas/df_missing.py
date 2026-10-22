# import pandas as pd
# # df =pd.read_excel("sales_dataset_50.xlsx")
# # # print(df.head())

# # # print(df.isna())

# # # print(df.isna().sum())

# # # print(df.isna().sum().sum())


# # print(df[df.isna().any(axis=1)])




# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Mouse"],
#     "Revenue": [50000, None, 20000, None]
# }

# df = pd.DataFrame(data)

# # df["Revenue"] = df["Revenue"].fillna(0)
# # df["Revenue"] = df["Revenue"].fillna(df["Revenue"].mean())
# df = df.dropna(subset=["Revenue"])

# print(df)


# import pandas as pd

# df = pd.read_excel("sales_dataset_50.xlsx")

# print("Before cleaning:")
# print(df.isna().sum())

# # Missing Revenue values ko mean se fill karo
# df["Revenue"] = df["Revenue"].fillna(df["Revenue"].mean())

# print("\nAfter cleaning:")
# print(df.isna().sum())
