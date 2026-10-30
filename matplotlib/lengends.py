import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [10000, 15000, 12000, 20000]
profit = [2000, 4000, 3000, 6000]

fig , ax = plt.subplots(figsize=(8,5))
ax.plot(months,sales, label="sales",marker="o")
ax.plot(months,profit, label="profit",marker="^")

ax.set_title("Monthly sales and profit")
ax.set_xlabel("months")
ax.set_ylabel("Amount")

ax.legend(
    loc="upper left",
    title="Performance",
    fontsize=10,
    frameon=True
)
plt.show()
