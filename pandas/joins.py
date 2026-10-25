import pandas as pd

# students = pd.DataFrame({
#     "Name": ["Aman", "Rahul", "Priya"]
# }, index=[1, 2, 3])

# marks = pd.DataFrame({
#     "Marks": [85, 90, 78]
# }, index=[1, 2, 3])

# print("Students DataFrame:")
# # print(students)

# print("\nMarks DataFrame:")
# # print(marks)

# result = students.join(marks)

# print(result)

# students = pd.DataFrame({
#     "Name": ["Aman", "Rahul", "Priya"]
# }, index=[1, 2, 3])

# marks = pd.DataFrame({
#     "Marks": [85, 90, 95]
# }, index=[1, 3, 4])

# result = students.join(marks, how="left")

# print(result)

import pandas as pd

A = pd.DataFrame({
    "Name": ["A", "B", "C"]
}, index=[1, 2, 3])

B = pd.DataFrame({
    "Salary": [10000, 20000, 30000]
}, index=[2, 3, 4])

# result = A.join(B, how="left")

# print(result)

# result = A.join(B, how="right")
# print(result)

result = A.join(B, how="inner")
print(result)