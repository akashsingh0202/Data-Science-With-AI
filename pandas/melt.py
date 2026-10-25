# # import pandas as pd

# # df = pd.DataFrame({
# #     "Name": ["Aman", "Priya"],
# #     "Math": [80, 90],
# #     "English": [75, 85]
# # })

# # long_df = df.melt(
# #     id_vars=["Name"],
# #     var_name="Subject",
# #     value_name="Marks"
# # )

# # print(long_df)


# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Aman", "Priya", "Rahul"],
#     "Math": [80, 90, 70],
#     "English": [75, 85, 65],
#     "Science": [88, 92, 78]
# })

# result=df.melt(
#     id_vars=["Name"],
#     # value_vars=["Math","Science"],
#     var_name="Subject",
#     value_name="Marks"
# )

# print(result)

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Priya", "Rahul"],
    "Math": [80, 90, 70],
    "English": [75, 85, 65]
}, index=[10, 20, 30])

# result = df.melt(
#     id_vars=["Name"],
#     var_name="Subject",
#     value_name="Marks",
#     ignore_index=False
# )

# print(result)


result=df.melt(
    id_vars="Name",
    value_vars="English",
    var_name="Subject",
    value_name="Marks",
    ignore_index=False
)
