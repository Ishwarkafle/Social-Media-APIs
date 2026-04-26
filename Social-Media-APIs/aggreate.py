#aggregate Fynction

import pandas as pd
df=pd.read_csv("data.csv",index_col="Name")
print(df["Height"].mean())
print(df["Height"].max())
print(df["Height"].min())
print(df["Height"].sum())

print(df.mean(numeric_only=True))
print(df.count())
grooupby_type = df.groupby("Type1")
print(grooupby_type["Height"].mean())
print(grooupby_type["Height"].max())
print(grooupby_type["Height"].min())    
print(grooupby_type["Height"].sum())
print(grooupby_type["Height"].count())  