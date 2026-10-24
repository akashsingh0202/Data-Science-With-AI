import pandas as pd

customers = pd.read_excel(
    "pandas/customers_dataset.xlsx",
    sheet_name="Customers"
)

orders = pd.read_excel(
    "pandas/orders_dataset.xlsx",
    sheet_name="Orders"
)

products = pd.read_csv(
    "pandas/products_dataset.csv"
)

print(customers.head())
print(orders.head())
print(products.head())