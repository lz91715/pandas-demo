import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index = dates, columns = ['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print df

# how = {'any', 'all'}
print df.dropna(axis = 1, how = 'any')

print df.fillna(value = 0)

print df.isnull()

print np.any(df.isnull() == True)
