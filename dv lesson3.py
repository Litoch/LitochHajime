import numpy as np
import pandas as pd

# 1
data1 = np.random.randint(3, 10, 5, dtype=int)
print(data1)
s1 = pd.Series(data1, index = ['a', 'b', 'c', 'd', 'e'])
print(s1)

# 2
print(s1[2:5])
print(s1['c':'e'])

# 3
data_dict = {'year':np.arange(2017,2020), 'price':np.linspace(10,30,3, dtype=int)}
df1 = pd.DataFrame(data_dict, index=[0,1,2])
print(df1)

# 4
data2 = np.random.randint(5, 15, 15, dtype=int).reshape(5,3)
print(data2)
df_test = pd.DataFrame(data2, index=['a', 'c', 'e', 'f', 'h'],
                       columns=['one', 'two', 'three'])
print(df_test)

# 5
df_test.loc['a', 'one'] = ""
df_test.loc['c', 'two'] = -99
df_test.loc['c', 'three'] = -99
df_test.loc['a', 'two'] = -100
df_change =  df_test.reindex(columns = ['one', 'two', 'three', 'four'],fill_value='test')
df_change = df_change.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df_test)
print(df_change)

# 6
print(df_change.dropna())

# 7
print(df_change.dropna(how = 'all'))

# 8
print(df_change.fillna(0))

# 9
print(df_change.drop_duplicates(keep=False))
