import pandas as pd


# 1
path = '/Users/litoch/info/lesson/task6_1.csv'
df1 = pd.read_csv(path)
print(df1)

# 2
print(pd.pivot_table(df1, index=['id'], columns=['date'],
                     values=['sales'], fill_value=0, aggfunc=np.sum))

# 3
print(pd.pivot_table(df1, index=['id'], columns=['date'],
                     values=['sales'], fill_value=0, aggfunc=np.sum, margins=True).iloc[0:-1,:])

# 4
path = '/Users/litoch/info/lesson/task6_2.csv'
df2 = pd.read_csv(path)
print(df2)

# 5
print(pd.pivot_table(df2, index=['sex','smoke'], values=['age', 'height']))

# 6
print(pd.crosstab(df2.sex, df2.smoke))

# 7
print(pd.crosstab(df2.age, df2.smoke))
