import pandas as pd

# students = pd.DataFrame({
#     "RollNo": [1, 1, 2],
#     "Name": ["Aman", "Amit", "Rahul"]
# })

# marks = pd.DataFrame({
#     "RollNo": [1, 1, 2],
#     "Marks": [80, 85, 90]
# })

# result = pd.merge(students, marks, on="RollNo", how="inner")

# print(result)

students = pd.DataFrame({
    "RollNo": [5, 5, 5],
    "Name": ["A", "B", "C"]
})

marks = pd.DataFrame({
    "RollNo": [5, 5],
    "Marks": [70, 90]
})

result = pd.merge(students, marks, on="RollNo", how="inner")
print(result)