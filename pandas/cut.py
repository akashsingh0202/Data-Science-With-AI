# import pandas as pd

# marks = [15, 28,30, 35, 48, 55, 67, 75, 89, 95]

# result = pd.cut(
#     marks,
#     bins=[0, 30, 60, 100],
#     labels=["Low", "Medium", "High"]
# )
import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Priya", "Rahul", "Neha", "Karan"],
    "Age": [18, 25, 35, 50, 65]
})
df["agegroup"]=pd.cut(
    df["Age"],
    bins=[0, 30, 60, 100],
    labels=["Low", "Medium", "High"],
    include_lowest=True
)

print(df)