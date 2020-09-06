import numpy as np
import pandas as pd

# 1
data_dict = {
    'marketcap': [449, 371, 237, 21313, 1369, 823],
    'pe': [8.31, 15.36, 16.01, 7.16, 7.59, 6.3],
    'code': ['600926', '002958', '601128', '601398', '601229', '600919']
}
index = ['杭州银行', '青农商行', '常熟银行', '工商银行', '上海银行', '江苏银行']
df_company = pd.DataFrame(data_dict, index=index)
print(df_company)

# 2
print(df_company.loc[df_company['marketcap']<2000])

# 3
condition1 = df_company['marketcap'] < 2000
condition2 = df_company['pe'] < 10
print(df_company.loc[condition1 & condition2])

# 4
dr = pd.date_range(start='2019-01-02', periods=100)
data = np.random.randn(100).cumsum()
close = data - np.min(data)
df = pd.DataFrame({"close": close}, index=dr)
print(df)

df['mov_avg'] = df['close'].rolling(5).mean()
print(df)

# 5
data2 = np.arange(1,17).reshape(4,4)
df2 = pd.DataFrame(data2, index=['a', 'b', 'c', 'd'], columns=['1st', '2nd', '3rd', '4th'])
print(df2)

# 6
df2['sum'] = df2.apply(lambda x: x.sum(), axis=1)
print(df2)

# 7
df2['extra_col'] = df2.apply(lambda x: x[0]+x[1] if x[2] > 10 else x[2], axis=1)
# def func1(x, y, z):
#     if z > 10:
#         return x + y
#     else:
#         return z
# df2['extra_col'] = df2.apply(lambda x: func1(x[0], x[1], x[2]), axis=1)
print(df2)
