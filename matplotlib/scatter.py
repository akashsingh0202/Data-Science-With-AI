import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 80, 90]

fig , ax = plt.subplots(figsize=(8,5))


ax.scatter(
    hours,
    marks,
    color="green",
    s=120,
    marker="o",
    alpha=0.6
)

ax.set_title("Student hous v/s Student marks")
ax.set_xlabel("Student hours")
ax.set_ylabel("Student Marks")

plt.show()
