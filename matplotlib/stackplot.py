import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

python_sales = [10, 15, 20, 25]
sql_sales = [5, 10, 15, 20]
powerbi_sales = [8, 12, 10, 18]

x = range(len(months))

fig, ax = plt.subplots(figsize=(8, 5))

ax.stackplot(
    x,
    python_sales,
    sql_sales,
    powerbi_sales,
    labels=["Python", "SQL", "Power BI"],
    alpha=0.7
)

ax.set_xticks(x, months)
ax.set_title("Monthly Product Sales")
ax.set_xlabel("Months")
ax.set_ylabel("Sales")

ax.legend(loc="upper left")
plt.show()