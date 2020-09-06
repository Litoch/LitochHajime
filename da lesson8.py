import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 1
path = '/Users/litoch/info/lesson/houses.csv'
df1 = pd.read_csv(path, encoding='gbk')
# print(df1.info())
print(df1)
df1.drop_duplicates(inplace=True)
# print(df1.info())

# 2
print("总房源数量：")
print(len(df1['title'].unique()))
print('总小区数量')
print(len(df1['xiaoqu_name'].unique()))
print('总板块数量')
print(len(df1['sub_district_name'].unique()))

# 3
print("户型情况：")
print(df1['huxing'].value_counts())
print('\n装修情况：')
print(df1['zhuangxiu'].value_counts())
print('\n建造年份情况：')
print(df1['buildyear'].value_counts())

# 4
print('上海二手房每平米均价：')
print(df1['up_price'].mean())

# 5
house_type = df1.groupby(['huxing'])['size'].agg(['count','mean']).sort_values(by='count', ascending=False)
print(house_type)

# 6
count_by_community = df1['xiaoqu_name'].value_counts(ascending=False)
print('\n每个小区房源数量：')
print(count_by_community)

# 7
avgprice_by_community = df1.groupby(['xiaoqu_name'])['up_price'].mean().sort_values(ascending=False)
print('\n每个小区每平方米均价：')
print(avgprice_by_community)

# 8
price_top5 = df1[['title','price']].sort_values(by='price', ascending=False)[:4]
print('总价top5')
print(price_top5)

# 9
df1.buildyear = pd.to_datetime(df1.buildyear, format='%Y')
count_by_title = df1.groupby(['buildyear'])['title'].count()
print('\n每10年各房源数量')
print(count_by_title.resample('10A').sum())
