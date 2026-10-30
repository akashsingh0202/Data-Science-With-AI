# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [10000, 15000, 12000, 20000]

# fig, ax = plt.subplots(figsize=(8, 5))

# ax.plot(months, sales, marker="o")

# ax.set_title("Monthly Sales")
# ax.set_xlabel("Months")
# ax.set_ylabel("Sales")

# ax.grid(
#     visible=True,
#     axis="y",
#     color="gray",
#     linestyle="--",
#     linewidth=0.8,
#     alpha=0.6
# )

# plt.show()

import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
profit = [2000, 4000, 3000, 6000, 8000]


fig, ax = plt.subplots(figsize=(8,5))

ax.plot(months,profit,marker="o")

ax.set_title("Revenue")
ax.set_xlabel("Profit")
ax.set_ylabel("Month")

ax.grid(
    axis="y",
    color="black",
    linestyle="--",
    alpha=0.5
)

plt.show()