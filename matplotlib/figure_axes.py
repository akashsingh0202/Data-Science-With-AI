import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10000, 15000, 12000, 20000]
profit = [2000, 4000, 3000, 6000]

fig, ax = plt.subplots(2, 1, figsize=(4, 10))

ax[0].plot(months, sales, marker="o")
ax[0].set_title("Monthly Sales")

ax[1].bar(months, profit)
ax[1].set_title("Monthly Profit")

fig.suptitle("Business Performance")

plt.tight_layout()
plt.show()