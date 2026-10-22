import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Priya", "Neha"],
    "Age": [22, 25, 21, 24],
    "Salary": [25000, 40000, 28000, 35000]
})

# print(df.sort_values(by="Salary"))
# print(df.sort_values(by="Salary", ascending=False))

print(df.sort_values(by=["Salary", "Age"]))