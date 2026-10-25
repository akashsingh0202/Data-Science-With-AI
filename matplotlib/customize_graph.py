import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 200]

plt.plot(
    months,
    sales,
    color="red",
    linestyle="-",
    linewidth=2,
    marker="o"
)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Report")
plt.show()