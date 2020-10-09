import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1
path = '/Users/litoch/info/lesson/task_3.1_zhihu_timeline_answer.csv'
pd.set_option('display.max_columns', 20)
zhihu_data_answer = pd.read_csv(path)
print(zhihu_data_answer.head())

# 2
x1 = list(zhihu_data_answer['回答点赞数'])
y1 = list(zhihu_data_answer['回答感谢数'])
fig,ax = plt.subplots(1,1,figsize=(5,5), facecolor='#e0ebd0')
ax.set_title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
ax.scatter(x1, y1, color='#45a282', marker='.')
'''
# 如果做拟合/fitting
p1 = np.polyfit(x1,y1,1)    # get the parameter
x1_ndarray = np.array(x1)
x1_float = x1_ndarray.astype(np.float)  # 转为float ndarray才可相乘
y1_fit = p1[0] * x1_float +p1[1]
ax.plot(x1_float,y1_fit,color='red')
'''

# 3
x2 = zhihu_data_answer['问题回答数'].tolist()
y2 = zhihu_data_answer['问题关注数'].tolist()
fig,ax = plt.subplots(1,1,figsize=(5,5), facecolor='#e0ebd0')
ax.set_title('Scatter Plot 2')
plt.xlabel('X2')
plt.ylabel('Y2')
ax.scatter(x2, y2, color='#45a282', marker='.')

# 4
path = '/Users/litoch/info/lesson/task_3.2_zhihu_timeline_article.csv'
pd.set_option('display.max_columns', 20)
zhihu_data_article = pd.read_csv(path)
zhihu_data_article.head()

# 5
x3 = zhihu_data_article['文章点赞数'].tolist()
y3 = zhihu_data_article['文章评论数'].tolist()
fig,ax = plt.subplots(1,1,figsize=(5,5), facecolor='#e0ebd0')
plt.scatter(x3, y3, c='#45a282', marker='.')


# 6
x4 = zhihu_data_article['文章点赞数'].loc[zhihu_data_article['文章点赞数']<1000]
fig,ax = plt.subplots(1,1,figsize=(5,5), facecolor='#e0ebd0')
plt.boxplot(x4)
plt.show()
