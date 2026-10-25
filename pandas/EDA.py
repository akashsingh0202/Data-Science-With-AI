# import pandas as pd

# df = pd.DataFrame({
#     "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone"],
#     "City": ["Rewa", "Bhopal", "Rewa", "Indore", "Bhopal"],
#     "Quantity": [2, 5, 1, 3, 4],
#     "Revenue": [100000, 75000, 50000, 45000, 60000]
# })

# print(df)
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())


import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Phone", "Laptop"],
    "City": ["Rewa", "Bhopal", "Indore", "Bhopal", "Rewa"],
    "Revenue": [50000, 20000, None, 20000, 50000]
})

# print(df)
print(df.isnull().sum())
print(df.duplicated().sum())