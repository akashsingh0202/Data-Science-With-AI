import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Priya", "Rahul", "Neha"],
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [30000, 50000, 20000, 40000]
})

df["DeptAvgSalary"] = (
    df.groupby("Department")["Salary"]
      .transform("mean")
)

print(df)