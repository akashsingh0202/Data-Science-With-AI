import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")

# city_summary = df.groupby(
#     "City",
#     as_index=False
# )["Revenue"].sum()

# # print(city_summary)

# high_revenue_cities = city_summary[
#     city_summary["Revenue"] > 200000
# ]

# print(high_revenue_cities)

city_summary = df.groupby(
    "City", as_index=False
)["Revenue"].sum()

result = city_summary[
    city_summary["Revenue"] > 100000
].sort_values("Revenue", ascending=False)

print(result)