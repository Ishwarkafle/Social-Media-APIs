import numpy as np
import pandas as pd

s = pd.Series([1, 2, np.nan])
print(s)
print(s.isna())
print(s.dropna())

s = pd.Series(['apple', 'banana', 'cherry'])

print(s.str.upper())