import matplotlib
import matplotlib.pyplot as plt

# print(matplotlib.__version__)
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [10000, 15000, 12000, 20000, 25000]

plt.plot(months, sales)
plt.show()