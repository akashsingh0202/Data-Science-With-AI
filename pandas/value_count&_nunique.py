import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")

# print(df["PaymentMode"].value_counts())
# print(df["PaymentMode"].nunique())

# print("Payment Mode Counts:")
# print(df["PaymentMode"].value_counts())

# print("\nTotal Unique Payment Modes:")
# print(df["PaymentMode"].nunique())

# print("\nCity Counts:")
# print(df["City"].value_counts())

print(df["PaymentMode"].value_counts(normalize=True) * 100)