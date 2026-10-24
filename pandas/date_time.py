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


# df = pd.DataFrame({
#     "Product": ["Laptop", "Mobile", "Tablet"],
#     "SaleDate": ["2026-01-10", "2026-04-15", "2026-08-20"]
# })
# # print(df)

# df["SaleDate"]=pd.to_datetime(df["SaleDate"],errors="coerce")

# # print(df.dtypes)
# # df["Year"] = df["SaleDate"].dt.year
# # df["Month"] =df["SaleDate"].dt.month
# # df["Day"] = df["SaleDate"].dt.day
# # df["MonthName"] = df["SaleDate"].dt.month_name()
# # print(df)
# df["Weekday"] = df["SaleDate"].dt.day_name()
# # print(df)
# print(df)

# df["SaleDate"] = pd.to_datetime(df["SaleDate"])

# result = df[df["SaleDate"] > "2026-06-01"]

# print(result)

# result = df[
#     (df["SaleDate"] >= "2026-01-01") &
#     (df["SaleDate"] <= "2026-04-30")
# ]

# print(result)


# df["SaleDate"] = pd.to_datetime(df["SaleDate"], errors="coerce")
# df["DayNumber"] = df["SaleDate"].dt.dayofweek
# df["DayOfYear"] = df["SaleDate"].dt.dayofyear
# df["DayOfMonth"]=df["SaleDate"].dt.daysofmonth


# print(df)

# df["FormattedDate"] = df["SaleDate"].dt.strftime("%d-%m-%Y")

# print(df[["SaleDate", "FormattedDate"]])


dates = pd.date_range(
    start="2026-01-01",
    end="2026-01-05",
    freq="D"
)

# print(dates)
# print(pd.date_range("2026-01-01", periods=4, freq="MS"))


# start_date = pd.to_datetime("2026-01-10")
# end_date = pd.to_datetime("2026-01-20")

# difference = end_date - start_date

# print(difference)
# print(difference.days)


# df["DeliveryDate"] = df["SaleDate"] + pd.Timedelta(days=7)

# print(df[["Product", "SaleDate", "DeliveryDate"]])


# df["MonthName"] = df["SaleDate"].dt.month_name()
# df["Quarter"] = df["SaleDate"].dt.quarter

# print(df[["Product", "MonthName", "Quarter"]])


# df = pd.DataFrame({
#     "SaleDate": ["2026-01-10", None, "invalid"]
# })

# df["SaleDate"] = pd.to_datetime(
#     df["SaleDate"],
#     errors="coerce"
# )

# print(df)
# print(df["SaleDate"].isna().sum())


#  parctice set

import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet"],
    "SaleDate": ["2026-01-10", "2026-04-15", "2026-08-20"]
})

df["SaleDate"] = pd.to_datetime(df["SaleDate"])
# MonthName=df["Monthname"]= df["SaleDate"].dt.month_name()
# print(MonthName)


# quarter1=df["Quarter"]=df["SaleDate"].dt.quarter
# print(quarter1)


# df["DeliveryDate"]=df["SaleDate"]+pd.Timedelta(days=10)
# print(df[["Product","SaleDate","DeliveryDate"]])

# df["FormattedDate"]=df["SaleDate"].dt.strftime("%d/%b/%Y")

# print(df[["SaleDate","FormattedDate"]])

# betweenDate=pd.date_range(
#     start="2026-01-01",
#     end="2026-03-31",
#     freq="D"
# )
# print(betweenDate)


# df["MonthName"]=df["SaleDate"].dt.strftime("%b")
# print(df["MonthName"])


# df["deliveryDate"]=df["SaleDate"]+pd.Timedelta(days=7)
# print(df[["SaleDate","deliveryDate"]])

dailyDates=pd.date_range(
    start="2026-01-01",
    end="2026-01-31",
    freq="D"
)
print(dailyDates)
