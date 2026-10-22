import pandas as pd


df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Priya", "Neha"],
    "Age": [22, 25, 21, 24],
    "Salary": [25000, 40000, 28000, 35000]
})

# print(df[df["Age"]>23])
# print(df[(df["Age"]>23) &(df["Salary"] > 35000)])
# print(df[(df["Age"] < 22) | (df["Salary"] > 40000)])

# print(df[df["Salary"].between(25000, 35000)])
print(df[df["Age"].isin([21, 24])])