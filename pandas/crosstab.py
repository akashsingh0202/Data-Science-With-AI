import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")

# report = pd.crosstab(
#     df["City"],
#     df["PaymentMode"]
# )

# print(report)

report = pd.crosstab(
    df["City"],
    df["PaymentMode"],
    values=df["Revenue"],
    aggfunc="sum"
).fillna(0)

print(report)