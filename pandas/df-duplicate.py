
import pandas as pd

df = pd.read_excel("sales_dataset_50.xlsx")

# Har row duplicate hai ya nahi
# print(df.duplicated())

# Total duplicate rows
print("Total duplicates:", df.duplicated().sum())
