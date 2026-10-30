import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv("customer_product_data_100_rows.csv",encoding="cp1252")
# print(df)
# plt.hist(df["Age"],bins=10)
plt.title("Demo chart")
plt.xlabel("Age")
plt.ylabel("count")
# plt.boxplot(df["Age"],patch_artist=True,meanline=True)
# plt.hist(x=df["Age Group"],bins=10)
# plt.show()

x=df["Product_Category"].value_counts()
colors=['red','orange','black','green','blue','yellow','purple','pink','skyblue']
# plt.bar(x.index, x.values ,color=colors)
# plt.show()


plt.pie(x.values,labels=x.index,autopct='%1.2f%%')
plt.show()