import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")

# df["PaymentMode"] = df["PaymentMode"].map({
#     "Cash": "C",
#     "UPI": "U",
#     "Card": "CD"
# })

# print(df["PaymentMode"])

# df["Revenue_Double"] = df["Revenue"].apply(
#     lambda x: x * 2
# )

# print(df["Revenue_Double"])

# df["Revenue_Status"] = df["Revenue"].apply(
#     lambda x: "High" if x > 5000 else "Low"
# )

# print(df[["Revenue", "Revenue_Status"]].head(10))
# print(df["PaymentMode"].unique())


payment_map = {
    "Credit Card": "CC",
    "Net Banking": "NB",
    "Debit Card": "DC",
    "UPI": "UPI",
    "Cash": "Cash"
}

df["Payment_Code"] = df["PaymentMode"].map(payment_map)

print(df[["PaymentMode", "Payment_Code"]].head(10))