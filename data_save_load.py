import numpy as np
import pandas as pd

# save data use to_xxx, ie. to_pickle('file') to_csv('file')
# load data use read_xxx, ie. read_pickle('file') read_csv('file')

data = pd.read_csv('students.csv')
print data

data.to_pickle('students.pickle')

data2 = pd.read_pickle('students.pickle')
print data2
