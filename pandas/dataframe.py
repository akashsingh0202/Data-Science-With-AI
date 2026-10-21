import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Age": [20, 21, 19],
    "Marks": [85, 72, 91]
}

df = pd.DataFrame(data)

# print(df)
print(df["Marks"])