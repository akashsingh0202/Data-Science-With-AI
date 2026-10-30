import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [10000, 15000, 12000, 20000]
profit = [2000, 4000, 3000, 6000]

plt.plot(
    months, sales,
    color="blue",
    marker="o",
    label="Sales"
)

plt.plot(
    months, profit,
    color="green",
    marker="s",
    label="Profit"
)

plt.title("Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")

plt.legend()
plt.grid(True)
plt.show()