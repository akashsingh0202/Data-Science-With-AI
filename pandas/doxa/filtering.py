import pandas as pd

df=pd.read_excel("pandas/sales_dataset_50.xlsx")
# print(df)


# accessing single row
# print(df.loc[3])

# accessing multiple row  it dosent exclude stop value
# print(df.loc[0:4])


# .accessing single  rows and single column
# print(df.loc[3,'SalesID'])

#  accessing multiple row and  single column
# we can do indexing and slicing for both rows and columns 
# print(df.loc[0:4,'City'])


#  accessing multiple rows and multiple column
# print(df.loc[0:10,'SalesID':'Category'])


#  iloc --> in iloc we need to pass only col names otherwise it will throw error 
#  loc function will add stop position as weel and we need to pass only column names to it 
# iloc will exclude stop position and we need to pass column index value to it 


#  Filtering 
# print(df[df["Quantity"]>3])


# city=df[(df["City"]=="Hyderabad")&(df["Category"]=="Electronics")]
# print(city)

# city=df[df["City"].isin(["Hyderabad","Pune"])]
# print(city)



# Sorting
# sort1=df.sort_values(by="Quantity",ascending=False)
# print(sort1)




# # data transformation  -- future engineering 
# def func(x):
#     if x>=5:
#         return "premium"

#     elif x>=3:
#         return "Gold"

#     else:
#         return "Silver"

# df["Stauts"]=df["Quantity"].apply(func)
# print(df)

# print(df.info())

df["new"]=df["Quantity"].apply(lambda x:"Premium" if x>=5  else "Gold"
                               if x>=3 else "silver")
print(df)