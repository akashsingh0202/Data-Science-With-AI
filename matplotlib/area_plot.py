# # import matplotlib.pyplot as plt

# # months = ["Jan", "Feb", "Mar", "Apr"]
# # sales = [10000, 15000, 12000, 20000]

# # x = range(len(months))

# # fig, ax = plt.subplots(figsize=(8, 5))

# # ax.plot(x, sales, marker="o", label="Sales")

# # ax.fill_between(
# #     x,
# #     sales,
# #     color="skyblue",
# #     alpha=0.4
# # )

# # ax.set_xticks(x, months)
# # ax.set_title("Monthly Sales Area Chart")
# # ax.set_xlabel("Months")
# # ax.set_ylabel("Sales")

# # ax.legend()
# # ax.grid(alpha=0.3)

# # plt.show()

# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr"]

# sales = [10000, 15000, 20000, 25000]
# expenses = [5000, 8000, 12000, 15000]

# x = range(len(months))

# fig, ax = plt.subplots(figsize=(8, 5))

# ax.plot(x, sales, label="Sales")
# ax.plot(x, expenses, label="Expenses")

# ax.fill_between(
#     x,
#     sales,
#     expenses,
#     alpha=0.3,
#     color="green"
# )

# ax.set_xticks(x, months)
# ax.set_title("Sales vs Expenses")
# ax.set_xlabel("Months")
# ax.set_ylabel("Amount")

# ax.legend()
# plt.show()


import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]

sales = [10000, 15000, 20000, 25000]
expenses = [5000, 8000, 12000, 15000]
fig , ax =plt.subplots(figsize=(8,5))
x=range(len(months))
ax.plot(x,sales,label="Sales")
ax.plot(x,expenses,label="Expenses")
ax.fill_between(
    x,
    sales,
    expenses,
    alpha=0.5,
    color="green"
)

ax.set_title("Monthly Revenue Growth")
ax.set_xlabel("Months")
ax.set_ylabel("Amount")
ax.legend()
ax.grid(alpha=0.5)
plt.show()




