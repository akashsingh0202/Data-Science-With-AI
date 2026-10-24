import pandas as pd

# employees = pd.DataFrame({
#     "EmployeeID": [1, 2, 3],
#     "Name": ["Aman", "Rahul", "Priya"]
# })

# salaries = pd.DataFrame({
#     "EmployeeID": [1, 2, 4],
#     "Salary": [25000, 30000, 40000]
# })

# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID"
# # )

# # print(result)

# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID",
# #     how="inner"
# # )

# # print(result)


# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID",
# #     how="left"
# # )

# # print(result)



# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID",
# #     how="right"
# # )

# # print(result)



# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID",
# #     how="outer"
# # )

# # print(result)



# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID",
# #     how="inner"
# # )







# # employees1 = pd.DataFrame({
# #     "EmployeeID": [1, 2, 3],
# #     "Name": ["Aman", "Rahul", "Priya"]
# # })

# # salaries1 = pd.DataFrame({
# #     "ID": [1, 2, 4],
# #     "Salary": [25000, 30000, 40000]
# # })
# # result = pd.merge(
# #     employees1,
# #     salaries1,
# #     left_on="EmployeeID",
# #     right_on="ID",
# #     how="inner"
# # )

# # print(result)


# # employees2 = pd.DataFrame({
# #     "EmployeeID": [1, 2],
# #     "Name": ["Aman", "Rahul"],
# #     "Department": ["IT", "HR"]
# # })

# # details = pd.DataFrame({
# #     "EmployeeID": [1, 2],
# #     "Department": ["Technology", "Human Resources"],
# #     "Salary": [25000, 30000]
# # })


# # result = pd.merge(
# #     employees2,
# #     details,
# #     on="EmployeeID",
# #     suffixes=("_employee", "_details")
# # )

# # print(result)


# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID",
# #     how="outer",
# #     indicator=True
# # )

# # print(result)




# employees = pd.DataFrame({
#     "EmployeeID": [1, 1],
#     "Name": ["Aman", "Aman Kumar"]
# })

# salaries = pd.DataFrame({
#     "EmployeeID": [1, 1],
#     "Salary": [25000, 30000]
# })

# # result = pd.merge(
# #     employees,
# #     salaries,
# #     on="EmployeeID",
# #     how="inner"
# # )

# # print(result)



# result = pd.merge(
#     employees,
#     salaries,
#     on="EmployeeID",
#     validate="one_to_one"
# )
# print(result)


# df1 = pd.DataFrame({
#     "Name": ["Aman", "Aman", "Rahul"],
#     "Year": [2025, 2026, 2025],
#     "Marks": [80, 90, 75]
# })

# df2 = pd.DataFrame({
#     "Name": ["Aman", "Rahul"],
#     "Year": [2026, 2025],
#     "Grade": ["A", "B"]
# })

# result = pd.merge(
#     df1,
#     df2,
#     on=["Name", "Year"],
#     how="inner"
# )

# print(result)
