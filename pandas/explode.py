# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Aman", "Priya", "Rahul"],
#     "Subjects": [
#         ["Math", "Science"],
#         ["English", "Hindi"],
#         ["Math", "Computer", "English"]
#     ]
# })

# # print(df)
# result = df.explode("Subjects")
# print(result)

import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Aman", "Priya", "Rahul"],
#     "Skills": [
#         ["Python", "SQL", "Pandas"],
#         ["Excel", "Power BI"],
#         ["Python"]
#     ],
#     "City": ["Rewa", "Bhopal", "Indore"]
# })

# result=df.explode("Skills",ignore_index=True)
# print(result)
# df = pd.DataFrame({
#     "Name": ["Aman", "Priya"],
#     "Skills": [["Python", "SQL"], []]
# })

# result = df.explode("Skills")
# print(result)


df = pd.DataFrame({
    "Name": ["Aman", "Priya"],
    "Skills": [["Python", "SQL"], ["Excel", "Power BI"]],
    "Level": [["Beginner", "Advanced"], ["Beginner", "Intermediate"]]
})

result = df.explode(["Skills", "Level"], ignore_index=True)
print(result)