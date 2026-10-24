import pandas as pd

df=pd.read_excel("pandas/sales_dataset_50.xlsx")
# df["PaymentMode"] = df["PaymentMode"].replace(
#     "Cash", "Cash Payment"
# )



# df["PaymentMode"]=df["PaymentMode"].replace(
#     "UPI","UPIs"
# )
print(df["PaymentMode"].value_counts())
df["PaymentMode"] = df["PaymentMode"].replace({
    "Cash": "Cash Payment",
    "UPI": "UPI Payment"
})
# print(df["PaymentMode"].head(5))
print(df["PaymentMode"].value_counts())