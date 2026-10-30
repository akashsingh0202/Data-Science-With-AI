import matplotlib.pyplot as plt

# categories = ["Rent", "Food", "Travel", "Shopping"]
# expenses = [20000, 15000, 10000, 5000]

# fig,ax=plt.subplots(figsize=(7,7))

# ax.pie(
#     expenses,
#     labels=categories,
#     autopct="%1.1f%%",
#     startangle=90,
#     explode = (0.1, 0, 0, 0)
# )
# ax.set_title("Monthly Expenses")
# plt.show()

subjects = ["Python", "SQL", "Power BI", "Statistics"]
hours = [40, 30, 20, 10]

fig,ax=plt.subplots(figsize=(7,7))

ax.pie(
    hours,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90,
    explode=(0.1,0,0,0)
    )


ax.set_title("Study Time Distribution")
plt.show()