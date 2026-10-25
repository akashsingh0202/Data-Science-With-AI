import pandas as pd

employees = pd.DataFrame({
    "Employee": ["Aman", "Rahul", "Priya"],
    "DeptID": [101, 102, 103]
})

departments = pd.DataFrame({
    "DeptName": ["HR", "IT", "Sales"]
}, index=[101, 102, 104])

# print(employees)
# print(departments)

result = employees.join(
    departments,
    on="DeptID",
    how="left"
)

print(result)