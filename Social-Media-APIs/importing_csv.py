import pandas as pd
df=pd.read_csv("data.csv",index_col="Name")


#print(df.to_string())
print(df.index)

print(df.loc["Bulbasaur"])

print(df.loc["Bulbasaur", ["Type1", "Type2"]])
print(df.loc["Bulbasaur":"Charizard", ["Type1", "Type2"]])

print(df.iloc[0:21:2,0:3])
