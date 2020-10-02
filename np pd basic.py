import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

plt.show()
%matplotlib inline

# 创建数组
# create an array
'''
numpy数组 -- ndarray
ndarray.ndim - 数组的轴（维度）的个数，也被称为rank
shape(n, m) -- n行，m列
ndarray.size -- 数组元素总数
ndarray.dtype
ndarray.itemsize -- 数组中每个元素的字节大小
'''
arr1 = np.array([[1,2], [3,4]], dtype=float)
arr1 = np.arange(4, dtype=float).reshape(2,2) # 0到4
# type(arr1) -- numpy.ndarray


# 全为0
arr2 = np.zeors((6,6), dtype=int)
# 全为1
arr3 = np.ones((6,6), dtype=int)
# 单位矩阵
arr4 = np.eye(6, dtype=int)
# 等差数列
arr5 = np.arange(0,10,2)	# 间隔/差为2， 包含0不包含10
# arange与浮点参数一起用时，难以控制所获得的元素数量
np.arange( 0, 2, 0.3 )                 
>>> array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
arr6 = np.linspace(0,10,6, dtype=int)	# 确保生成6个数字
>>> array([ 0,  2,  4,  6,  8, 10])
# 四则运算都可以直接运算
A + B
# 矩阵内元素一一对应乘法
A * B
# 矩阵乘法
A @ B
A.dot(B)
# 可一元操作
# 对数组中所有元素进行操作
arr.sum()
arr.min()
arr.max()
# 按轴(axis)操作
b = np.arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
# 按列求和 sum of each column
b.sum(axis=0)
>>>
array([12, 15, 18, 21])
# 每行最小值 min of each row
b.min(axis=1)
>>>
array([0, 4, 8])
# 每行累计求和 cumulative sum along each row
b.cumsum(axis=1)
>>>
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])

'''
不想让numpy省略打印中间部分的场合：
np/set_printoptions(threshold=sys.maxsize)
'''
# 生成随机数/random
np.random.randint(100, size=10)
np.random.randint(1,100,[5,5]) 	# (1,100)范围内5行5列随机整数
np.random.rand(2,3) 	# 2行3列均匀分布(0,1)范围随机数
np.random.randn(3,3)	# 3行3列正态分布随机数
np.random.random(3)
>>>
array([0.71675453, 0.90394818, 0.62290411])
np.random.random((2,3))		# 相当于np.random.rand(2,3)
>>>
array([[0.88977193, 0.75928207, 0.02648582],
       [0.97543119, 0.45690348, 0.40242845]])

np.argmax(arr)	# 返回最大值的索引
np.argmin(arr)
np.argmax(arr, axis=1)	# 返回每行的最大值的索引
[[11 18 14 45 10]
 [24 77 31 78 56]]
 >>>
 array([3, 3])
# 欧式距离
np.linalg.norm(a-b)
# 设置seed
np.random.seed(0)


# 读取/read/load
with open(path, encoding='utf-8') as f:
	data = np.loadtxt(path, delimiter=',')
	print(data[:5])

np.loadtxt(path, delimiter=',', dype=str, skiprows=1, usecols=(0,2,1,3))
# dtype=str, 以str形式读取数据
# skiprows=1：跳过第一行
# usecols：读取特定的列。(0,2,1,3) -- 第二和第三列互换
# 取前5行
print(data[:5])
# 取前5行第3列
print(data[:5, 2])
# 取具体的第5行第3列
print(data[5, 2])
# 取第3列
print(data[:, 2])
print(type(data))
>>>
<class 'numpy.ndarray'>

x = [4, 6, 2, 1, 7, 9]
# 改变x
x.sort(reverse=True)
# 不改变x
y = sorted(x, reverse=True)
np.unique(arr)
'''
return_index=True
return_inverse=True
return_counts=True
'''
arr.mean(axis=0)
arr.var()
arr.std()
arr.cumsum()

'''
！！！numpy 空值：np.nan
df.loc['a','one'] = np.nan

Series
Pandas数据类型，带标签（index？）的一位数组，与numpy中的array类似
可以保存任何数据类型（int、str、float、python object etc.）
pd.Series(data, index, dtype)
1. data可以是字典，字典的key就是index
2. 由数组创建
3. 由标量创建
'''

s = pd.Series(np.random.rand(5))
print(s.index)
>>>
RangeIndex(start=0, stop=5, step=1)

s = pd.Series(10, index = range(4))
>>>
0    10
1    10
2    10
3    10
dtype: int64


df.loc['a', 'one'] = np.nan
df.iloc[1, 3] = -99		# 原始索引

df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                            columns = ['one', 'two', 'three', 'four'],
                            fill_value='test')

# method = 'ffill'/'bfill'

df.isnull()	#是缺失值返回True，否则范围False
df.isnull().sum()	#返回每列包含的缺失值的个数
df.dropna()	#直接删除含有缺失值的行
df.dropna(axis = 1)	#直接删除含有缺失值的列
df.dropna(how = 'all')	#只删除全是缺失值的行
df.dropna(thresh = 4)	#保留至少有4个缺失值的行
df.dropna(subset = ['C'])#	删除含有缺失值的特定的列
df.fillna(0)	#用0填充
df.fillna(method='pad') #用前一个数值填充
df.fillna(df2.mean())	#用该列均值填充

# 删除重复行
df_change.drop_duplicates(keep=False)


# 读取csv文件
df = pd.read_csv('path')
df.to_csv('file_name')

# 显示
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 1000)


# 读取excel文件
df = pd.read_excel('index300.xls', sheet_name='Price Return Index', index_col=0)
print(df.head())
print(df.tail())
print(df.index)
print(df.index.names)
print(df.columns)
print(df.values)
print(df.info())
print(df.describe())

df.loc[index_name, col_name]
df.loc[3] # index名称3
# 选行标签
df.loc['a', 'b', 'f']
df.loc['c':'h']
df.loc[df.A>0.5]
df.loc[df.A>0.5,['C', 'D']]
df.loc[lambda df:df.A>0.5]


