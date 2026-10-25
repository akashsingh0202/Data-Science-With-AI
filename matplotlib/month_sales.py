# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [100, 150, 120, 200]

# plt.plot(months, sales)

# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Monthly Sales Report")

# plt.show()

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [10000, 15000, 12000, 20000, 25000]

plt.plot(
    months,
    sales,
    color="green",
    linestyle="--",
    linewidth=2,
    marker="o",
    markersize=8
)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Report")

plt.show()