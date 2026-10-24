import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")
# print(df)

# df = df.rename(columns={
#     "SalesDate": "Sale_Date",
#     "PaymentMode": "Payment_Mode"
# })
# print(df.columns)


df=df.rename(columns={
    "SalesDate":"Sales_Date",
    "PaymentMode":"Payment_Mode",
    "Revenue":"Total_Revenue"

})
print(df.columns)