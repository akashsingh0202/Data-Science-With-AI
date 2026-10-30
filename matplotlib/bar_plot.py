import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Headphones"]
sales = [50000, 30000, 20000, 10000]

fig , ax=plt.subplots(figsize=(8,5))

ax.bar(products,sales,color="Red",width=0.5)

ax.set_title("Product Sales")
ax.set_xlabel("Product")
ax.set_ylabel("Sales")

plt.show()