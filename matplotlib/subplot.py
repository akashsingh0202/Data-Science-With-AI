import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10000, 15000, 12000, 20000]

ax.plot(months, sales, color="green", marker="o")
ax.set_title("Monthly Sales")
ax.set_xlabel("Months")
ax.set_ylabel("Sales")

plt.show()