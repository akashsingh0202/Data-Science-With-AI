import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Priya", "Rahul"],
    "DepartmentCode": ["IT", "HR", "IT"]
})

department_map = {
    "IT": "Information Technology",
    "HR": "Human Resources"
}

df["Department"] = df["DepartmentCode"].map(department_map)

print(df)


marks = pd.Series([20, 30, 40])

result = marks.map(lambda x: x + 5)

print(result)