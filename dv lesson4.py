import pandas as pd

# 1
path = '/Users/litoch/info/lesson/sh.600000.csv'
df = pd.read_csv(path)

# 2
print(df.head())
print(df.tail())

# 3
# pd.set_option('display.max_rows', 100)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_columns', 20)
print(df.info())
print(df.describe())

# 5 (No Q4?)
print(df.columns)

# 6.1
print(df.iloc[0:3])
print(df.loc[0:2])

# 6.2
print(df['date'])
print(type(df['date']))

# 6.3
print(df[['date','open','close']])
print(type(df[['date','open','close']]))

# 6.4
print(df.loc[df['close']>11.08])

# 6.5
df1 = df.set_index('date')
print(df1)
print(df1.loc['2017-12-11':'2017-12-20'])

# 6.6
print(df1.loc[:, 'open':'close'])

# 6.7
print(df1.loc['2018-07-01':'2018-07-08','open':'close'])
