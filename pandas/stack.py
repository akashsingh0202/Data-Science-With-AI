# import pandas as pd

# # df = pd.DataFrame({
# #     "Name": ["Aman", "Rahul"],
# #     "Math": [80, 90],
# #     "Science": [85, 95]
# # })

# # print(df)
# # result = df.set_index("Name").stack()
# # print(result)

# # back = result.unstack()
# # print(back)



# df = pd.DataFrame({
#     "Department": ["IT", "IT", "HR", "HR"],
#     "Employee": ["Aman", "Rahul", "Priya", "Neha"],
#     "Salary": [50000, 60000, 40000, 45000]
# })

# multi_df = df.set_index(["Department", "Employee"])

# result = multi_df.unstack(level=0)
# print(result)

# df = pd.DataFrame({
#     "Department": ["IT", "IT", "HR", "HR"],
#     "Employee": ["Aman", "Rahul", "Priya", "Neha"],
#     "Salary": [50000, 60000, 40000, 45000]
# })

# multi_df = df.set_index(["Department", "Employee"])

# result = multi_df.unstack(level=0)
# print(result)

# import pandas as pd

# df = pd.DataFrame({
#     "Department": ["IT", "IT", "HR", "HR"],
#     "Employee": ["Aman", "Rahul", "Priya", "Neha"],
#     "Salary": [50000, 60000, 40000, 45000]
# }) 
# multi_df=df.set_index(["Department","Employee"])
# result=multi_df.unstack(level=0)
# print(result)

