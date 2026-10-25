import pandas as pd
# marks = [10, 20, 30, 40, 50, 60, 70, 80]

# result = pd.qcut(
#     marks,
#     q=4,
#     labels=["Q1", "Q2", "Q3", "Q4"]
# )
# print(result)

import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
    "Age": [18, 25, 35, 50, 65]
})

result=pd.cut(
    bins=[0, 20, 40, 100],
    labels=["Young", "Adult", "Senior"]

)