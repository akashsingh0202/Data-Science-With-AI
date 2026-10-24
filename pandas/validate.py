import pandas as pd

# employees = pd.DataFrame({
#     "EmployeeID": [1, 2, 3],
#     "Name": ["Aman", "Rahul", "Priya"]
# })

# salaries = pd.DataFrame({
#     "EmployeeID": [1, 2, 3],
#     "Salary": [25000, 30000, 35000]
# })

# result = pd.merge(
#     employees,
#     salaries,
#     on="EmployeeID",
#     how="inner",
#     validate="one_to_one"
# )

# print(result)


# employees = pd.DataFrame({
#     "EmployeeID": [1, 2],
#     "Name": ["Aman", "Rahul"]
# })

# projects = pd.DataFrame({
#     "EmployeeID": [1, 1, 2],
#     "Project": ["FinTrack", "HireFlow", "SalesApp"]
# })

# result = pd.merge(
#     employees,
#     projects,
#     on="EmployeeID",
#     how="left",
#     validate="one_to_many"
# )

# print(result)

# transactions = pd.DataFrame({
#     "EmployeeID": [1, 1, 2, 2],
#     "Amount": [500, 800, 300, 900]
# })

# employees = pd.DataFrame({
#     "EmployeeID": [1, 2],
#     "Name": ["Aman", "Rahul"]
# })
# result = pd.merge(
#     transactions,
#     employees,
#     on="EmployeeID",
#     how="left",
#     validate="many_to_one"
# )

# print(result)



left = pd.DataFrame({
    "ID": [1, 1],
    "Name": ["Aman", "Rahul"]
})

right = pd.DataFrame({
    "ID": [1, 1],
    "Score": [80, 90]
})

result = pd.merge(
    left,
    right,
    on="ID",
    validate="many_to_many"
)

print(result)
