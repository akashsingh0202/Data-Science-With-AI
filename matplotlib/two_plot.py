import matplotlib.pyplot as plt 


months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10000, 15000, 12000, 20000]
profit = [2000, 4000, 3000, 6000]

fig, ax=plt.subplots(1,2,figsize=(10,4))

#  first graph
ax[0].plot(months, sales, marker="o", color="green")
ax[0].set_title("Monthly Sales")
ax[0].set_xlabel("Months")
ax[0].set_ylabel("Sales")


# second graph
ax[1].bar(months,profit,color='orange')
ax[1].set_title('monthly profit')
ax[1].set_xlabel('Months')
ax[1].set_ylabel('Profit')


plt.tight_layout()
plt.show()