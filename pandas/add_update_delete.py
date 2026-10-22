import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Aman", "Rahul", "Priya"],
#     "Age": [22, 25, 21],
#     "City": ["Rewa", "Bhopal", "Indore"]
# })
# # add column
# df["Salary"] = [25000, 30000, 28000]
# # # add column with same value
# df["Country"] = "India"

# # # Existing column update karna
# # df["Age"] = df["Age"] + 1


# # # Column delete karna
# # df = df.drop(columns=["City"])
# # df = df.drop(columns=["Age", "Salary"])

# #  add new student
# df.loc[len(df)] = {
#     "Name": "Neha",
#     "Age": 24,
#     "City": "Rewa",
#     "Salary": 32000,
#     "Country": "India"
# }

# df = df.drop(index=1)

# print(df)

df = pd.DataFrame({
    "Name":["Aman","Rahul","Priya"],
    "Age":[22,25,21]
})
df["City"]=["Rewa","Bhopal","Indore"]
df["Age"]=df["Age"]+2
df=df.drop(index=1)
df["Passed"]="Yes"
df = df.reset_index(drop=True)
print(df)
