import pandas as pd
df=pd.read_excel("pandas/sales_dataset_50.xlsx")
# print(df)
# print(df.head())
# print(df.head(10))
# print(df.tail())
# print(df.tail(10))
# print(df.sample())
# print(df.sample(10))
# print(df.info())
# print(df.info(10))
# print(df.describe())
# print(df.describe(include='object'))


# result_df = []
# for col in df.columns:
#    result_df.append(col.strip())


# df.rename(columns={'SalesDate':'Date'},inplace = True)
# print(df.head())

# df.drop(columns=['Revenue'],inplace=True)
# print(df.head())

# ref_df = df.copy()
# print(ref_df)



# df['UnitPrice'] = df['UnitPrice'].astype('int32')
# print(df.dtypes)


# df['Revenue'] = pd.to_numeric(df['Revenue'],errors ='coerce')
# print(df)


# df['Date'] = pd.to_datetime(df['Date'],errors = 'coerce')
# print(df)

# print(df.isnull().sum())


print(df.shape)