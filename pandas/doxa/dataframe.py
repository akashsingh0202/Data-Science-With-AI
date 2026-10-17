#dataframe:
import pandas as pd

#2d data where in the form of rows and columns

d = {

     'names':['ajay','rohit','shyam','rahul'],
     'age':[20,30,40,50],
     'marks':[100,90,80,70]
}
# print(d)
df = pd.DataFrame(d)
# print(df)
# print(df.describe())