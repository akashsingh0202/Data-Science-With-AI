
import pandas as pd

# Series: single column
marks = pd.Series([85, 72, 91])

# DataFrame: multiple columns
df = pd.DataFrame({
    "Name": ["Rahul", "Aman", "Priya"],
    "Marks": [85, 72, 91]
})

print("Series:")
print(marks)

print("\nDataFrame:")
print(df)
print(df.marks())
