import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot([1, 2, 3], [10, 20, 15])

ax.set_title("My First Graph")
ax.set_xlabel("X values")
ax.set_ylabel("Y values")

plt.show()