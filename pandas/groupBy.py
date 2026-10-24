import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")


# # city_sales = df.groupby("City")["Revenue"].sum()

# # print(city_sales)
# # Har city ka total revenue
# sum_sales=df.groupby("City")["Revenue"].sum()

# # Har city ka average revenue
# mean_sales=df.groupby("City")["Revenue"].mean()

# # Har city mein revenue entries count karna
# count_sales=df.groupby("City")["Revenue"].count()


# city_summary = df.groupby("City")["Revenue"].agg(
#     ["sum", "mean", "max", "min"]
# )

# print(city_summary)
# multiple_column=df.groupby(["City", "PaymentMode"])["Revenue"].sum()
# print(multiple_column)

# city_payment_summary = df.groupby(
#     ["City", "PaymentMode"]
# )["Revenue"].agg(["sum", "mean", "count"])

# print(city_payment_summary)