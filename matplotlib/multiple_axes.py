# import matplotlib.pyplot as plt

# fig, axes = plt.subplots(2, 1, figsize=(10, 4))

# axes[0].plot([1, 2, 3], [10, 20, 15],marker="o")
# axes[0].set_title("Graph 1")

# axes[1].plot([1, 2, 3], [5, 15, 25],marker="o")
# axes[1].set_title("Graph 2")

# plt.show()


import matplotlib.pyplot as plt

# fig, axes = plt.subplots(2, 2, figsize=(8, 6),squeeze=False)
fig, axes = plt.subplots(2, 2, figsize=(8, 6),sharex=True)

axes[0, 0].plot([1, 2, 3], [10, 20, 30])
axes[0, 0].set_title("Graph 1")

axes[0, 1].plot([1, 2, 3], [30, 20, 10])
axes[0, 1].set_title("Graph 2")

axes[1, 0].plot([1, 2, 3], [5, 15, 25])
axes[1, 0].set_title("Graph 3")

axes[1, 1].plot([1, 2, 3], [10, 10, 20])
axes[1, 1].set_title("Graph 4")

plt.tight_layout()
plt.show()