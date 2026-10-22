import pandas as pd

# data = {
#     "Product": ["Laptop", "Mobile", "Laptop", "Mouse"],
#     "City": ["Rewa", "Bhopal", "Rewa", "Indore"],
#     "Revenue": [50000, 20000, 50000, 1000]
# }

# df = pd.DataFrame(data)

# print(df.drop_duplicates())

df=pd.read_excel("pandas/sales_dataset_50.xlsx")
# print(df)

# # Duplicate rows remove karo
# df_clean = df.drop_duplicates()

# print("Before:", len(df))
# print("After:", len(df_clean))

# # Index ko reset karna optional hai
# df_clean = df_clean.reset_index(drop=True)
print(df.duplicated().sum())
print(df.drop_duplicates())