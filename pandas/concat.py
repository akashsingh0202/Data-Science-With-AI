import pandas as pd

df1 = pd.DataFrame({
    "City": ["Mumbai", "Delhi"],
    "Revenue": [1000, 2000]
})

df2 = pd.DataFrame({
    "City": ["Pune", "Jaipur"],
    "Revenue": [3000, 4000]
})
df3 = pd.DataFrame({
    "City": ["Pune", "Jaipur"],
    "total_revenue": [3000, 4000]
})

# # result1 = pd.concat([df1, df2],ignore_index=True, axis=1)
# result2 = pd.concat([df1, df2],ignore_index=True, axis=0)

# # print(result1)
# print(result2)

# result3 = pd.concat(
#     [df1, df3],
#     join="outer",
#     ignore_index=True
# )

# print(result3)

# result4 = pd.concat(
#     [df1, df3],
#     join="inner",
#     ignore_index=True
# )

# print(result4)


# result5 = pd.concat(
#     [df1, df2],
#     keys=["January", "February"]
# )

# print(result5)


# result6 = pd.concat(
#     [df1, df3],
#     verify_integrity=True
# )

# print(result6)