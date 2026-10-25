# # # import pandas as pd

# # # df = pd.DataFrame({
# # #     "City": ["Rewa", "Rewa", "Bhopal", "Bhopal"],
# # #     "Year": [2025, 2026, 2025, 2026],
# # #     "Sales": [10000, 15000, 20000, 25000]
# # # })

# # # # print(df)

# # # multi_df = df.set_index(["City", "Year"])

# # # print(multi_df)

# # import pandas as pd

# # df = pd.DataFrame({
# #     "Department": ["IT", "IT", "HR", "HR"],
# #     "Employee": ["Aman", "Rahul", "Priya", "Neha"],
# #     "Salary": [50000, 60000, 40000, 45000]
# # })

# # multi_df = df.set_index(["Department", "Employee"])

# # # print(multi_df)

# # # result=multi_df.loc["IT"]

# # # result = multi_df.reset_index()
# # # print(result)
# # # result = multi_df.loc[("HR", "Neha")]
# # # print(result)

# # # swapped = multi_df.swaplevel("Department", "Employee")
# # # swapped = multi_df.swaplevel(0, 1)
# # # print(swapped)

# # # sorted_df = multi_df.sort_index()
# # sorted_df = multi_df.sort_index(level=1)
# # print(sorted_df)


# # import pandas as pd

# # df = pd.DataFrame({
# #     "Department": ["IT", "IT", "HR", "HR"],
# #     "Employee": ["Aman", "Rahul", "Priya", "Neha"],
# #     "Salary": [50000, 60000, 40000, 45000]
# # })

# # multi_df = df.set_index(["Department", "Employee"])

# # print(multi_df)
# # print(multi_df.index.get_level_values(0))

# # print(multi_df.index.get_level_values("Department").unique())

# # it_employees = multi_df[
# #     multi_df.index.get_level_values("Department") == "IT"
# # ]

# # print(it_employees) 

# # hr_employee=multi_df[
# #     multi_df.index.get_level_values("Department")=="HR"
# # ]


# # result = multi_df[
# #     multi_df.index.get_level_values("Employee") == "Aman"
# # ]

# # print(result)








# import pandas as pd

# df = pd.DataFrame({
#     "Department": ["IT", "IT", "HR", "HR"],
#     "Employee": ["Aman", "Rahul", "Priya", "Neha"],
#     "Salary": [50000, 60000, 40000, 45000]
# })

# multi_df = df.set_index(["Department", "Employee"])

# # print(multi_df)


# # result = multi_df.droplevel("Department")
# result = multi_df.droplevel(1)
# print(result)




import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Employee": ["Aman", "Rahul", "Priya", "Neha"],
    "Salary": [50000, 60000, 40000, 45000]
})

# multi_df = df.set_index(["Department", "Employee"])
# result=multi_df.loc["IT"]


multi_df = df.set_index(["Department", "Employee"])
multi_df.sort_values(by="Salary")




