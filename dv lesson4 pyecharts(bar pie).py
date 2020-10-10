import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyecharts.charts import Bar, Pie, Page, Grid
from pyecharts import options as opts

# 1
path = '/Users/litoch/info/lesson/Task_4_lianjia_sale.csv'
pd.set_option('display.max_columns', 20)
df = pd.read_csv(path)
print(df.head())

df_avg = df.groupby(['区域'])['价格'].agg([('平均房价', 'mean')]).sort_values(by = '平均房价')
print(df_avg)
print(df_avg.head())

# 2
x1 = df_avg.index.values.tolist()
y1 = df_avg['平均房价'].tolist()
bar = (
    Bar(init_opts=opts.InitOpts(width='1000px'))
    .add_xaxis(x1)
    .add_yaxis('平均房价',y_axis=y1)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='上海各区域平均价格'))
)
bar.render(path='/Users/litoch/info/lesson/df1 avg.html')
# plt.show()

# 3
df_zhuangxiu = df.groupby(['装修类型'])['区域'].agg([('房源数量', 'count')])
print(df_zhuangxiu)

# 4
label = df_zhuangxiu.index.values.tolist()
data = df_zhuangxiu['房源数量'].tolist()

pie = (
    Pie()
    .add('', [list(z) for z in zip(label, data)])
    .set_global_opts(title_opts=opts.TitleOpts(title='装修类型占比情况'))   # zip -- 打包成tuple
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))  # 格式化标签输出内容
)
pie.render(path='/Users/litoch/info/lesson/df2 avg.html')

'''
v1=["啤酒","可乐","雪碧","咖啡","奶茶"]
v2=[30,19,21,12,18]
a = [list(z) for z in zip(v1,v2)]
a
>>> [['啤酒', 30], ['可乐', 19], ['雪碧', 21], ['咖啡', 12], ['奶茶', 18]]
'''
