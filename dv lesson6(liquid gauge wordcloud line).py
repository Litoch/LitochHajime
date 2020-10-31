import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyecharts.charts import Liquid, Gauge, WordCloud, Line
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ThemeType
import tushare as ts

# 1
pd.set_option('display.max_columns', 100)
df = ts.get_stock_basics()

liquid1 = (Liquid()
         .add('lq', [df['gpr'].mean()/100, 0.3],shape='roundRect',is_outline_show=False)
        # 水球外形，有' circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow' 可选
        # 默认 'circle'。也可以为自定义的 SVG 路径
        # is_outline_show设置边框
        .set_global_opts(title_opts=opts.TitleOpts(title="gpr")))
liquid1.render(path='/Users/litoch/info/lesson/Liquid1.html')

gauge1=(Gauge()
        .add("", [("",round(df['npr'].mean(), 2))], min_=-100)
        .set_global_opts(title_opts=opts.TitleOpts(title="npr"))
)
gauge1.render(path='/Users/litoch/info/lesson/Gauge1.html')


# 2
df1 = ts.get_stock_basics()
df_industry = df1.groupby(['industry'])['industry'].agg([('行业公司数量', 'count')])
list_industry = df_industry.index.tolist()
list_count = df_industry['行业公司数量'].values.tolist()
print(df_industry)
words = [list(z) for z in zip(list_industry, list_count)]
wordcloud = (
    WordCloud()
    .add('', words, word_size_range=[20,100])
    .set_global_opts(title_opts=opts.TitleOpts(title='公司行业分布'))
)
wordcloud.render(path='/Users/litoch/info/lesson/wordcloud1.html')


# 3
df2 = ts.get_hist_data('600519')
high = df2['high'].tolist()
low = df2['low'].tolist()
date = df2.index.tolist()

# Pyecharts
line = (
    Line()
    .add_xaxis(date)
    .add_yaxis('High', high)
    .add_yaxis('Low', low)
    .set_global_opts(title_opts=opts.TitleOpts(title='茅台最高/最低价格'))
)
line.render(path='/Users/litoch/info/lesson/echartsline.html')

# matplotlib
plt.plot(date, low, color='#45a282', marker=',', linestyle='-')
plt.plot(date, high, color='#ff6f87', marker=',', linestyle='-')
plt.legend(('Low', 'High'), loc='upper right')
plt.title('茅台最高/最低价格')
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.show()
