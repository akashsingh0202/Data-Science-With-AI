import matplotlib.pyplot as plt

# products = ["Laptop", "Mobile", "Tablet", "Headphones"]
# sales = [50000, 30000, 20000, 10000]

# fig , ax = plt.subplots(figsize=(8,5))

# ax.barh(products,sales ,color="orange")

# ax.set_title("Product Sales")
# ax.set_ylabel("Product")
# ax.set_xlabel("Sales")

# plt.show()


students = ["A", "B", "C", "D", "E"]
marks = [85, 70, 90, 60, 75]

fig,ax=plt.subplots(figsize=(8,5))

ax.barh(students,marks,color="blue")
ax.set_title("Result")
ax.set_ylabel("Marks")
ax.set_xlabel("Students")

plt.show()