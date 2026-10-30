import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df=sns.load_dataset('tips')
# print(df.info())


# sns.histplot(x='tip',data=df , kde=True)
sns.boxplot(x='tip',data=df)
plt.show()


