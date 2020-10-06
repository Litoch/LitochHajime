import pandas as pd


# 1
path = '/Users/litoch/info/lesson/jobs.csv'
df = pd.read_csv(path)
# print(df.info())
df = df.drop_duplicates()
# print(df.info())
pd.set_option('display.max_columns', 20)
print(df.head())

# 2
print(df['source'].value_counts())
# the datatype of return is series

# 3
print(df['experience'].value_counts())

# 4
print(df['education'].value_counts())

# 5
print(df["company_type"].value_counts())

# 6
print('\nthe MEAN of salary:')
print(df['salary2'].mean())

# 7
top10_salary = df['salary2'].groupby(df['company']).mean().sort_values(ascending=False)[:10]
print(top10_salary)

# 8
top10_postion = df['company'].value_counts()[0:10]
print(top10_postion)

# 9
top10_salary_2 = df['salary2'].groupby(df['company_type']).mean().sort_values(ascending=False)[:10]
print(top10_salary_2)
