import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# sales = [10000, 15000, 12000, 20000, 25000]

# fig, ax = plt.subplots(figsize=(8, 4))

# ax.plot(months, sales, marker="o", color="green")

# ax.set_title("Monthly Sales Report")
# ax.set_xlabel("Months")
# ax.set_ylabel("Sales")

# ax.grid(True)

# plt.show()

months=["Jan", "Feb","Mar", "Apr"]
sales=[10000, 15000, 12000, 20000]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(
    months,
    sales,
    color="green",
    marker="o"
)

ax.set_xlabel("Months")
ax.set_ylabel("Sales")
ax.set_title("Monthly Sales")
ax.grid(True)
plt.show()
