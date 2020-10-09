import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1
path = '/Users/litoch/info/lesson/task_2_lianjia_data.csv'
pd.set_option('display.max_columns', 20)
lianjia_data = pd.read_csv(path)
print(lianjia_data.head())

# 2
area_amt = lianjia_data.groupby(['面积大小（㎡）'])['简介（方式·小区名 户型 朝向）'].agg([('房源数量','count')])
print(area_amt)
# print(lianjia_data.groupby(['面积大小（㎡）'])['面积大小（㎡）'].agg([('房源数量','count')]))

# 3
x1 = area_amt.index.values
y1 = area_amt['房源数量'].values.tolist()
line
plt.plot(x1, y1, 'c,-')
plt.plot(x1, y1, color='#45a282', marker=',', linestyle='-')
# histogram
plt.bar(x1, y1, alpha=0.8, width=0.5, color='#45a282')
fig, ax = plt.subplots(2,1)
ax[0].plot(x1, y1, color='#45a282', marker=',', linestyle='-')
ax[1].bar(x1, y1, alpha=0.8, width=0.5, color='#45a282')
ax[0].set_title('Line Chart')
ax[1].set_title('Bar Chart')
plt.tight_layout()

# 4
district_amt = lianjia_data.groupby(['区'])['区'].agg([('房源数量','count')])
print(district_amt)

# 5
x2 = district_amt.index.values
y2 = district_amt['房源数量'].tolist()
plt.bar(x2, y2, alpha=0.8, width=0.8, color='#45a282')
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #正常显示中文标签

# 6
floortype_amt = lianjia_data.groupby(['楼层类型'])['楼层类型'].agg([('房源数量', 'count')])
print(floortype_amt)

#7
x3 = floortype_amt.index.values
y3 = floortype_amt['房源数量'].tolist()
labels = ['Middle', 'Low', 'Base', 'High']
explode = (0.1,0,0,0)
colors=['#756477','#DECFCF', '#F6EEE8', '#EDA7A7']
plt.pie(y3, labels=labels, explode=explode, colors=colors, autopct='%.2f%%',
        pctdistance=0.7, shadow=False, labeldistance=1.13)
plt.rcParams['figure.figsize'] = (5.0, 5.0)
# plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #正常显示中文标签

plt.show()
