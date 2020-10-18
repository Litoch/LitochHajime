import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyecharts.charts import Bar, Pie, Page, Grid, Map, Geo
from pyecharts import options as opts
import tushare as ts

# print(ts.__version__)
#
# # # 设置token
# ts.set_token('d08d585617564dfc75c5e13285f10e3c74ec6c28eebeec9bf4700843')
# # # 初始化pro接口
# pro = ts.pro_api()
# # 如果无效
# # pro = ts.pro_api('d08d585617564dfc75c5e13285f10e3c74ec6c28eebeec9bf4700843')
#
# df = pro.stock_basic()
# print(df)

# 1
path = '/Users/litoch/info/lesson/Task_4_lianjia_sale.csv'
pd.set_option('display.max_columns', 20)
df = pd.read_csv(path)
print(df.head())

df_avg = df.groupby(['区域'])['价格'].agg([('平均房价', 'mean')]).sort_values(by = '平均房价')
print(df_avg)
print(df_avg.head())

districts = df_avg.index.values.tolist()
print(districts)

districts_a = []

for i in districts:
    if i == '浦东':
        districts_a.append(i+"新区")
    else:
        districts_a.append(i+'区')

print(districts_a)

price_avg = df_avg['平均房价'].tolist()
print(price_avg)

map_list = [[districts_a[i], price_avg[i]] for i in range(len(districts))]
print(map_list)
map1 = Map()
map1.set_global_opts(
    title_opts=opts.TitleOpts(title='上海各区房价均值'),
    visualmap_opts=opts.VisualMapOpts(max_=100000, is_piecewise=False)   # 最大数据范围
)
map1.add('上海各区房价均值', map_list, maptype='上海')
map1.render(path='/Users/litoch/info/lesson/map sh.html')


# 2
df2 = ts.get_stock_basics()
print(df2.head())

count_company = df2.groupby(['area'])['area'].agg([('公司数量', 'count')])
print(count_company)

districts2 = count_company.index.values.tolist()
companies = count_company['公司数量'].tolist()
map_list2 = [[districts2[i], companies[i]] for i in range(len(districts2))]

print(map_list2)
map2 = Map()
map2 = Map()
map2.set_global_opts(
    title_opts=opts.TitleOpts(title='上市公司数量'),
    visualmap_opts=opts.VisualMapOpts(max_=600, is_piecewise=False)   # 最大数据范围
)
map2.add('上市公司数量', map_list2, maptype='china')
map2.render(path='/Users/litoch/info/lesson/map ssec.html')
