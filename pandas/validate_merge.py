import pandas as pd

A = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Aman", "Rahul"]
})

B = pd.DataFrame({
    "ID": [1, 1, 2],
    "Marks": [80, 85, 90]
})

result = pd.merge(
    A, B,
    on="ID",
    validate="one_to_many"
)

print(result)