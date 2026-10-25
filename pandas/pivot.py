import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Aman", "Priya", "Priya"],
    "Subject": ["Math", "English", "Math", "English"],
    "Marks": [80, 75, 90, 85]
})

# result = df.pivot(
#     index="Name",
#     columns="Subject",
#     values="Marks"
# )

# result = df.pivot_table(
#     index="Name",
#     columns="Subject",
#     values="Marks",
#     aggfunc="mean"
# )

result = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Marks",
    aggfunc="sum",
    fill_value=0
)

print(result)