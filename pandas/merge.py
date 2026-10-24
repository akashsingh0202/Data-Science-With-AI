import pandas as pd

df1 = pd.DataFrame({
    "EmployeeID": [1, 2, 3],
    "Name": ["Aman", "Ravi", "Neha"]
})

df2 = pd.DataFrame({
    "EmployeeID": [1, 2, 4],
    "Salary": [30000, 40000, 50000]
})

# result = pd.merge(
#     df1,
#     df2,
#     on="EmployeeID"
# )

# print(result)

# result2=pd.merge(df1, df2, on="EmployeeID", how="inner")

# print(result2)

# result3=pd.merge(df1, df2, on="EmployeeID", how="left")
# print(result3)


# result4=pd.merge(df1, df2, on="EmployeeID", how="right")
# print(result4)

# result5=pd.merge(df1, df2, on="EmployeeID", how="outer")
# print(result5)

# result6=pd.merge(
#     df1,
#     df2,
#     on="EmployeeID",
#     suffixes=("_left", "_right")
# )
# print(result6)

# result7=pd.merge(
#     df1,
#     df2,
#     on="EmployeeID",
#     validate="one_to_one"
# )
# print(result7)
