# import pandas as pd

# marks = pd.Series([35, 60, 75, 90])

# def add_bonus(x):
#     return x + 5

# result = marks.apply(add_bonus)

# print(result)


import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Aman", "Priya", "Rahul", "Neha"],
#     "Marks": [92, 76, 45, 30]
# })

# def get_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 40:
#         return "C"
#     else:
#         return "Fail"

# df["Grade"] = df["Marks"].apply(get_grade)

# print(df)

# df = pd.DataFrame({
#     "Math": [80, 90, 70],
#     "Science": [70, 85, 60],
#     "English": [90, 75, 80]
# })
# print(df)
# result = df.apply(sum, axis=0)

# print(result)

# marks = pd.Series([10, 20, 30])

# result = marks.apply(lambda x: x * 2)

# print(result)


# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Aman", "Priya", "Rahul", "Neha"],
#     "Marks": [95, 72, 38, 85]
# })

# def get_grade(Marks):
#     if(Marks >= 90):
#         return "A"
#     elif Marks >= 75:
#         return "B"
#     elif Marks >= 40:
#         return "C"
#     else:
#         return "Fail"

# df["Grade"]=df["Marks"].apply(get_grade)
# print(df)


import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Priya", "Rahul"],
    "Math": [80, 90, 60],
    "Science": [70, 85, 75]
})

def calculate_total(row):
    return row["Math"] + row["Science"]

df["Total"] = df.apply(calculate_total, axis=1)

print(df)






