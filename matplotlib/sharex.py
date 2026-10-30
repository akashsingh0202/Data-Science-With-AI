import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales_2025 = [10000, 15000, 12000, 20000]
sales_2026 = [12000, 18000, 16000, 25000]

fig, ax = plt.subplots(
    2, 1,
    sharex=True,
    # sharey=True,
    figsize=(8, 6)
)

# First graph
ax[0].plot(months, sales_2025, marker="o", color="green")
ax[0].set_title("Sales 2025")
ax[0].set_ylabel("Sales")

# Second graph
ax[1].plot(months, sales_2026, marker="o", color="blue")
ax[1].set_title("Sales 2026")
ax[1].set_xlabel("Months")
ax[1].set_ylabel("Sales")

plt.tight_layout()
plt.show()