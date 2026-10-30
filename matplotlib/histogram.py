import matplotlib.pyplot as plt

fg , ax =plt.subplots(figsize=(8,5))
marks = [
    35, 40,20,10, 45, 50, 55,
    60, 65, 70, 75, 80,
    85, 90, 55, 65, 75,
    45, 50, 60, 70, 80,30,30
]
ax.hist(
    marks,
    bins=10,
    color="green" ,
    edgecolor="black",
    # rwidth=0.8
)

ax.set_title("Student Marks Distribution")
ax.set_xlabel("Marks")
ax.set_ylabel("Students")

plt.show()
