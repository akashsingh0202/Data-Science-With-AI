import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Priya", "Rahul", "Neha"],
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [30000, 50000, 20000, 40000],
    "Code": ["A", "B", "A", "B"]
})

def bonus_salary(salary):
    return salary + salary * 0.10

df["BonusSalary"] = df["Salary"].apply(bonus_salary)
status_map = {
    "A": "Active",
    "B": "Blocked"
}
df["Status"] = df["Code"].map(status_map)

df["DeptAvgSalary"] = (
    df.groupby("Department")["Salary"]
      .transform("mean")
)

print(df)