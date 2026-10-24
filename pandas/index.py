import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")

# city_summary = df.groupby("City")["Revenue"].sum().reset_index()

# print(city_summary)

# city_payment_summary = df.groupby(
#     ["City", "PaymentMode"],
#     as_index=False
# )["Revenue"].sum()

# print(city_payment_summary.head(10))

# print("Total Revenue:", df["Revenue"].sum())
# print("Average Revenue:", round(df["Revenue"].mean(), 2))
# print("Maximum Revenue:", df["Revenue"].max())
# print("Minimum Revenue:", df["Revenue"].min())
# print("Revenue Count:", df["Revenue"].count())