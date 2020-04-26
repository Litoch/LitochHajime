# ds note

# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# for fancier plot
import seaborn as sns
# instead of importing every model for scikit-learn
# we specify the functions we want out of the library
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# standardize/standardization 标准化
from sklearn.preprocessing import StandardScaler
# confusion matrix
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, \
    precision_recall_curve, roc_auc_score, roc_curve, precision_score, recall_score, \
    f1_score
# cross validation / kFold
from sklearn.model_selection import cross_val_score, KFold


# pandas
データの入出力（CSV, Excel, DB, HTML, etc...）
データの前処理（データの抽出,欠損値処理,ピボットテーブルしたりetc...）
簡易的な可視化（グラフを書いてimageとして保存,など）


# import/load data
data_file = '...route'
df = pd.read_scv(data_file)


# to show more
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)
df.head()
df.tail()


# show specific columns
df['Age', 'Sex', 'Survived']
my_columns = ['Age', 'Sex', 'Survived']
df[my_columns]

df2 = df[my_columns]
print(df2)


# size of df
print('Number of data points:', len(df))


# number of missing value
print(df.isnull().sum())

Number of data points: 891
Number of nulls in each column:
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

pd.isnull(df['Age']).value_counts()

False    714
True     177
Name: Age, dtype: int64

pd.notnull(df['Age']).value_counts(normalize=True)

True     0.801347
False    0.198653
Name: Age, dtype: float64


# 添加筛选条件/condition/filter
condition1 = df['Sex'] == 'female'
df.loc[condition1]
df.loc[condition1]['Survived'].value_counts(normalize=True)

condition2 = df['Age'] > 40
condition3 = df['Age'] < 50
(condition1 & condition2 & condition3).value_counts()

False    864
True      27
dtype: int64

df.loc[condition1 & condition2 & condition3]	# show dataframe
df.loc[condition1 & condition2 & condition3]['Survived'].value_counts()
df.loc[df['Sex']=='male']['Age'].mean()


# output the data
df3 = df.loc[condition1 & condition2 & condition3]
df3.to_csv('test_titanic_output.csv')

# histogram/柱状图/直方图
df['Age'].hist()
 

# 创建画布
# 散点图/scatter
# 画图/plot
fig, ax = plt.subplots()
ax.scatter(df['Age'], df['Fare'])

fig, ax = plt.subplot(2,1)	# 一张画布 两行一列/上下两张图
ax[0].hist(df.loc[df['Sex']=='male']['Age'], bins=80, range=(0,80))
ax[1].hist(df.loc[df['Sex']=='female']['Age'], bins=80, range=(0,80), color='pink')

ax[0].set_title('Histogram of age of men on Titanic')
ax[1].set_title('Histogram of age of women on Titanic')

fig, ax = plt.subplots()
X['Fare'].hist(ax=ax[0])
plt.hist(X_trans[:,1])


# change y-axis extent on second figure to match first one
# 更改图2 y轴的取值范围
ax[1].set_ylim(0,20)

# prevents subplots from overlapping
# 防止图像重叠
plt.tight_layout()


# 常见统计量
# mean, std, min, max
df['Age'].mean()
df['Age'].std()
df['Age'].min()
df['Age'].max()
df['Age'].describe()

count    714.000000
mean      29.699118
std       14.526497
min        0.420000
25%       20.125000
50%       28.000000
75%       38.000000
max       80.000000
Name: Age, dtype: float64


# fill in missing value
df['Age'] = df['Age'].fillna(df['Age'].median())


# count of categorical variable/个数
df['Embarked'].value_counts()

S    644
C    168
Q     77
Name: Embarked, dtype: int64


# percentage of categorical variable
df['Survived'].value_counts(normalize=True)

Percentage of survivors
0    0.616162
1    0.383838

Name: Survived, dtype: float64

# seaborn/sns/lmplot
# x_estimator: x 軸の各値に指定された関数を実行し、その返り値をプロットします
# そのプロットに対する回帰を可視化することができます
sns.lmplot(data=df, x='Pclass', y='Survived', x_estimator=np.mean)


# IsMale/增加一列判断
df['IsMale'] = df['Sex'] == 'male'
 

# show columns
df[['Sex', 'IsMale']]


# get dummy variable
Pclass_dummies = pd.get_dummies(df['Pclass'], prefix='Pclass')


# 合并
# axis=1: 放右侧。 axis=0: 放下方。
pd.concat([df['Pclass'], Pclass_dummies], axis=1)
 

# train, test, split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# 建立模型
# run model
# train dataset
model = LogisticRegression()
model.fit(X_train, y_train)


# predict/prediction model
# pred/proba
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

y_pred_proba
array([[0.82570289, 0.17429711],
       [0.83637322, 0.16362678],
       [0.82926508, 0.17073492],
       [0.24858047, 0.75141953],
       [0.31007752, 0.68992248],
       [0.18504583, 0.81495417],
       [0.34127194, 0.65872806],
       [0.80789217, 0.19210783],
       [0.32183637, 0.67816363],
       [0.2819867 , 0.7180133 ],
       ......


# the output of model.predict is a numpy array
# so convert it to a pandas series for convenience
# numpy ndarray -- 多维数组
# pandas series —— 一维数组， 具有index（索引）。支持从列表和字典创建
# dataframe —— 将数个series按列合并而成的二维数据结构，每一列单独取出来是一个series
# （和sql数据库中取出的数据类似）
# dataframe优势：可以方便地处理不同类型的列，因此不要考虑如何对一个全是float type的dataframe求逆
# 处理此类问题还是把数据存为numpy matrix比较便利
prob_series = pd.Series(y_pred_proba, name='SurvivalProbability', index=y_test.index)
X = df[['Age', 'Fare', 'IsMale']]
y = df['Survived']
pd.concat([X_test,prob_series, y_test], axis=1)

Age	Fare	IsMale	SurvivalProbability	Survived
709	28.0	15.2458	True	0.174297	1
439	31.0	10.5000	True	0.163627	0
840	20.0	7.9250	True	0.170735	0
720	6.0		33.0000	False	0.751420	1
39	14.0	11.2417	False	0.689922	1
290	26.0	78.8500	False	0.814954	1

# 取出test部分数据
test_df = df.loc[X_test.index]
test_df['SurvivalProbability'] = y_pred_proba	# 多添了suvivalprobability一列
test_df.iloc[1]	# 取出实际的第二行数据

PassengerId                                               440
Survived                                                    0
Pclass                                                      2
Name                   Kvillner, Mr. Johan Henrik Johannesson
Sex                                                      male
Age                                                        31
SibSp                                                       0
Parch                                                       0
Ticket                                             C.A. 18723
Fare                                                     10.5
Cabin                                                     NaN
Embarked                                                    S
Original_Age                                               31
IsMale                                                   True
TraveledAlone                                            True
SurvivalProbability                                  0.163627
Name: 439, dtype: object

# work out the score of model
# 计算模型正确率/得分
print(model.score(X_test, y_test))


# You should not always use a random seed, because then your test won't be truly random
# but if you want your results to be reproducible


# shape of dataframe
print(y_test.shape)
print(y_pred_proba.shape)


# standardize/standardization 标准化
ssc = StandardScaler()
X_trans = ssc.fit_transformation(X)


# model coefficient/模型系数
model.coef_


# confusion matrix in python scikit-learn
          Predicted
          0    1
Actual 0  TN   FP
       1  FN   TP

precision_recall_fscore_support(y_actual, y_pred)
# the second column will correspond to the precision and recall values that we're interested in
# the first column shows to the equivalent metrics if True corresponded to passenger death
# these metrics implicityly assume a particular cutoff for classification of 0.5


# ROC/sensitivity curve -- Receiver Operating Characteristic curve
# a technique that accounts for different possible boundaries/cutoff
[fpr, tpr, thresholds] = roc_curve(y_test, y_pred_proba)

plt.plot(fpr, tpr)
plt.title('Receiver Operatin Characteristic (ROC) Curve', fontsize=16)
plt.xlabel('FPR(False Positive Rate)', fontsize=14)
plt.ylabel('TPR(True Positice Rate)', fontsize=14)
# draw the "no-skill" line
# a bad classifier cannot distinguish between true positives and false positives
# thus the frequency of each would be about the same regardless of the choice of threshold
ply.plot([0,1], [0,1], color='gray', linestyle='--')


# AUROC -- Area Under ROC curve, the overall performance of a model
# the AUROC of the no-skill line is 0.5
# a model with perfect recall and no false positive would achieve a score of 1
# a score below 0.5 -- worse than random
score = roc_auc_score(y_test, y_pred_proba)
print("AUC score:", score)


# 提取列/list/column
column_2 = ['Age', 'Fare', 'TraveledAlone'] + list(Pclass_dummies.columns)
X_2 = df[column_2]


# do not feel obliged to change the decision threshold/cutoff from default value 0.5
# present an ROC curve and AUC score are more than sufficient
# choosing the thresold for classfication is an entirely separate problem from building a good model
# and there may not be be a single best choice
# seek optimize different metrics according to the context that the model is subsequently used in 
# e.g. 
# 1. whether to administer a invasive medical treatment: high precision, possibly at the expense of recall
# 2. in court where suspects are assumed innocent until proven guilty: be wary of false positive
# 3. political campaign, determine pamphlets to send to potential voters: high recall

# Youden ratio -- the maximal distance from the no-skill line
# solid intermediate metric that balances precision and recall
# calculated literally as TPR-FPR
# to show the max distance row in series
max_distance = pd.Series(tpr-fpr, name='Maximal Distance')
thresholds = pd.Series(thresholds, name='Threshold')
max_distance_df = pd.concat([max_distance, thresholds], axis=1)

max_distance_df

	Maximal Distance	Threshold
0		0.000000		1.898200
1		0.011236		0.898200
2		0.003773		0.823732
3		0.015009		0.823131
4		0.007547		0.819105
5		0.018782		0.692580

max_distance_df.loc[max_distance_df['Maximal Distance'] == max_distance_df['Maximal Distance'].max()]

	Maximal Distance	Threshold
52		0.484236		0.320011

# use the new threshold
threshold = .320
y_pred_final = y_pred_proba > threshold 	# True/False
pd.concat([y_pred, y_pred_final.astype(int)], axis=1)
# .astype() -- within numpy.ndarray, as well as the Pandas Series class
# so can be used to convert vectors, matrices and columns within a DATAFRAME


# Cross Validation
# by taking the average of a metric over all splits
# we get a performance estimate with much less noise
# quantify the uncertainty by taking the standard deviation
# downside: when having lots of data, training many models can be prohibitively slow

# K-folds cross validation
# data will be split into k segments/folds, k-1 foldsj will be used to train
# left 1 will be used to test
cv = KFold(n_splits=5)
# show test indices in each fold
for i, (train, test) in enumerate(cv.split(X, y)):
	print('Slice {}'.format(i+1))
	print('Test indices')
	print(test)
# show training indices in each fold
for i, (train,test) in enumerate(cv.split(X, y)):
	print('Slice {}'.format(i+1))
	print('Training indices')
	print(train)
# random order
cv = KFold(n_splits=5, shuffle=True)

# hide the details of how the data is split
# jump to give you performance statistics for each fold
# default metric: score
# in the case of logistic regression, default: accuracy
# obtain 95% confidence interval using the sd
classifier = LogisticRegression(solver='lbfgs')
# logistic solver
# small datasets -- liblinear	faster    for large datasets -- sag, saga
# multiclass, handle multinomial loss -- newton-cg, sag, saga, lbfgs
# one-versus-rest schemes -- liblinear
# L2 or no penalty -- newton-cg, lbfgs, sag, saga
# L1 penalty -- liblinear, penalty
# elasticnet penalty -- saga
# liblinear does not support setting penalty='none'
# L1 -- assigning insignificant input features with 0 weight: sparse solution
# L2 -- force the weights to be small but not zero: non-sparse solution,
# not robust to outliers
# performs better when all the input influence the output and all weights are of roughly equal size

scores = cross_val_score(classifier, X, y, cv=10)
print('Accuracy for each fold: ', scores)
print('Mean accuracy: {}'.format(scores.mean()))
print('Standard deviation:', scores.std())
print('95% confidence range: {}-{} '.format(scores.mean()-2*scores.std(), scores.mean()+2*scores.std()))

Accuracies for each fold: [0.57777778 0.6        0.69662921 0.73033708 0.65168539 0.64044944
 0.66292135 0.66292135 0.68539326 0.625     ]


# cross_val_score function does not have a way of shuffling the data
# if you want to control over which data goes into each of the folds, use KFold


# arange()类似于内置函数range()，通过指定开始值、终值和步长创建表示等差数列的一维数组，
# 注意得到的结果数组不包含终值。

# linspace()通过指定开始值、终值和元素个数创建表示等差数列的一维数组，
# 可以通过endpoint参数指定是否包含终值，默认值为True，即包含终值。
# scipy：处理插值、积分、优化、图像处理、常微分方程数值解的求解、信号处理

from scipy import interp
from sklearn.metrics import auc
roc_auc = auc(fpr, tpr)
roc_auc_score(y_test, y_pred_proba)

x = 2.5
xp = [1, 2, 3]
fp = [3, 2, 0]
y = np.interp(x, xp, fp)  # 1.0
plt.plot(xp, fp, '-o')
plt.plot(x, y, 'x')
plt.show()


# heatmap/correlation coefficient/相关系数/相关性
sns.heatmap(abs(df.corr()), vmin=0, vmax=1)		# non-negative
sns.heatmap(df.corr(), vmin=-1, vmax=1, venter=0)		# plot negative correlations in the blue, positivecorrelations in the red
sns.heatmap(abs(df.corr()), vmin=0, vmax=1, annot=True)		# show the actual magnitude of the correlation coefficient

# hnadling imbalanced data
# oversampling
!! TRAINING DATASET
1. choice of metric: F1-score -- which balances precision and recall
   AUC -- which iterates over all possible thresholds
   You have n poits in you majotiry, m points in your minority class
2. Downsampling: randomly select a subset of m points from the majority class
   -- dataset includes an equal number of points 2m from your majority and minority calsses
3. Upsampling: use points of from your minority class reapeatdly, 
   randomly choose one of the m points in the minority class, add it to your data set, repeat this process n times
   -- your data set ends up with 2n points
4. Weighting: change the error funtion in your algorithm
   -- errors in the classification of the minority class are weighted more heavily

Downsampling/Upsampling -- statistics technique: bootstrapping
Used when data is limited or cannot easily be fit by traditional statistical models
 ▼ For some problems, your data can be expanded by generating synthetic(a.k.a fake) data.
   -- Assuming you know enough about the underlying patterns in your data set
 ▼ Most of time, use some kind of bootstrap method to generate new data samples resampled from your existing data

!! TEST DATASET: 
in the same proportions as your real data
- otherwise, you are not testing your model performance realistically

# use built-in functions from numpy that generate random numbers to pick samples from majority and minority





