import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

delhi_sales = [10000, 15000, 12000, 20000]
mumbai_sales = [12000, 18000, 16000, 25000]

fig, ax = plt.subplots(
    1, 2,
    sharey=True,
    figsize=(10, 4)
)

# First graph
ax[0].plot(months, delhi_sales, marker="o", color="green")
ax[0].set_title("Delhi Sales")
ax[0].set_xlabel("Months")
ax[0].set_ylabel("Sales")

# Second graph
ax[1].plot(months, mumbai_sales, marker="o", color="blue")
ax[1].set_title("Mumbai Sales")
ax[1].set_xlabel("Months")

plt.tight_layout()
plt.show()