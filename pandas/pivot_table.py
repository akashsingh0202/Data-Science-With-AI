import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")

# city_report = pd.pivot_table(
#     df,
#     index="City",
#     values="Revenue",
#     aggfunc="sum"
# )

# print(city_report)

# payment_report = pd.pivot_table(
#     df,
#     index="PaymentMode",
#     values="Revenue",
#     aggfunc="sum"
# )

# print(payment_report)

# city_avg = pd.pivot_table(
#     df,
#     index="City",
#     values="Revenue",
#     aggfunc="mean"
# )

# print(city_avg)

# city_avg=pd.pivot_table(
#     df,
#     index="City",
#     values="Revenue",
#     aggfunc=["sum", "mean"]
# )

# print(city_avg)

report = pd.pivot_table(
    df,
    index="City",
    columns="PaymentMode",
    values="Revenue",
    aggfunc="sum",
    fill_value=0
)

# print(report)
print(report.shape)
# print(report.columns.tolist())
# print("Total columns:", len(report.columns))
