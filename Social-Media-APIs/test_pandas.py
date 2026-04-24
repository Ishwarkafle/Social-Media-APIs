import pandas as pd
data=[1,2,3,4,5,6,7,8,9,10]
series=pd.Series(data,index=['a','b','c','d','e','f','g','h','i','j'])
print(series.loc['d'])
series.loc['b']=67
print(series)
series=series[series>5]
print(series)

s = pd.Series([1,2,3,4])

print(s * 2)
print(s[s > 2])

s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([10,20,30], index=['b','c','d'])

print(s1 * s2)