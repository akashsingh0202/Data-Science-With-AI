import matplotlib.pyplot as plt
# marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 150]

# fig,ax=plt.subplots(figsize=(5,5))

# ax.boxplot(
#     marks,
#     patch_artist=True,
#     showmeans=True
# )

# ax.set_title("Student Marks Distribution")
# ax.set_ylabel("Marks")
salary = [20000, 22000, 25000, 27000, 30000,
          32000, 35000, 38000, 40000, 45000,
          50000, 55000, 150000]

fig, ax =plt.subplots(figsize=(8,5))
ax.boxplot(
    salary,
    patch_artist=True,
    showmeans=True,
)

ax.set_title("Employee Salary Distribution")
ax.set_ylabel("Salary")
plt.show()