# import pandas as pd

# students = pd.DataFrame(
#     {"Name": ["Rahul", "Aman", "Priya"]},
#     index=[1, 2, 3]
# )

# marks = pd.DataFrame(
#     {"Marks": [80, 90]},
#     index=[1, 2]
# )

# print(students)
# print(marks)


import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Aman", "Rahul", "Priya"],
#     "JoinDate": ["2025-01-15", "2025-06-20", "2026-03-10"]
# })

# print(df)
# print(df.dtypes)

# df["JoinDate"] = pd.to_datetime(df["JoinDate"])

# print(df.dtypes)

# df = pd.DataFrame({
#     "Date": ["2025-01-15", "hello", "2026-03-10"]
# })

# df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


df = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet"],
    "SaleDate": ["2026-01-10", "2026-04-15", "2026-08-20"]
})
print(df)

df["SaleDate"]=pd.to_datetime(df["SaleDate"],errors="coerce")

print(df.dtypes)