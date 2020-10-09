import pandas as pd

# 1
path = '/Users/litoch/info/lesson/task_1_zhaopin_data.csv'
pd.set_option('display.max_columns', 20)
df1 = pd.read_csv(path)
# 2
print(df1.head())
# 3
print(df1.tail())
# 4
print(df1[:3])
# 5
print(df1.iloc[2])
print(df1[2:3])
# 6
print(df1[['学历要求','工作经验','是否全职']])
# 7
df2 = df1.set_index('公司名')
print(df2.head())
# 8
df3 = df2.drop(columns=['其他备注'])
print(df3.head())
# 9
df4 = df3.drop(['上海蜗兴科技有限公司'], axis=0)
print(df4.head())
# 10
df4.to_csv('/Users/litoch/info/lesson/task_1_zhaopin_data_update.csv', encoding='utf-8-sig')
