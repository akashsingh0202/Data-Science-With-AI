import pandas as pd

# employees = pd.DataFrame({
#     "Name": ["Aman", "Rahul", "Priya"],
#     "DeptID": [101, 102, 103]
# })

# departments = pd.DataFrame({
#     "DeptID": [101, 102, 104],
#     "DeptName": ["HR", "IT", "Sales"]
# })

# #  merge
# result = pd.merge(
#     employees,
#     departments,
#     on="DeptID",
#     how="left"
# )

# print(result)

#  join
# departments_indexed = departments.set_index("DeptID")

# result1 = employees.join(
#     departments_indexed,
#     on="DeptID",
#     how="left"
# )

# print(result1)
import pandas as pd

students = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Priya"],
    "RollNo": [1, 2, 3]
})

marks = pd.DataFrame({
    "RollNo": [1, 2, 4],
    "Marks": [80, 90, 70]
})
result = pd.merge(
    students,
    marks,
    on="RollNo",
    how="left"
)

print(result)