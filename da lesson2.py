import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = '/Users/litoch/info/lesson/iris.csv'
with open(path) as f:
    data = np.loadtxt(path)

print(data)

# 2
min_point = np.argmin(data)
print('Min Position:', min_point)
max_point = np.argmax(data)
print('Min Position:', max_point)

# 3
print('Maximum:', np.max(data))
print('Minimum:', np.min(data))

# 4
data2 = sorted(data)
print(data2)

# 5
data3 = np.unique(data)
print(data3)

# 6
print('Mean:',np.mean(data))

# 7
print('Standard Deviation:', np.std(data))
print('Variance:', np.var(data))

# 8
print('Sum:', np.sum(data))

# 9
print('Cummulative Sum:', np.cumsum(data))

# 10
print('The # over 5.84:', (data > 5.84).sum())
