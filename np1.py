import numpy as np
import matplotlib.pyplot as plt

# 1
arr1 = np.arange(4, dtype=float).reshape(2,2)
print('arr1: ')
print(arr1)

# 2
arr2 = np.zeros((6,6), dtype = int)
print('arr2: ')
print(arr2)

arr3 = np.ones((6,6), dtype = int)
print('arr3: ')
print(arr3)

arr4 = np.eye(6, dtype = int)
print('arr4: ')
print(arr4)

# 3
arr5 = np.arange(0,10,2)
print('arr5: ')
print(arr5)

# 4
arr6 = np.linspace(0,10,6, dtype=int)
print('arr6: ')
print(arr6)

# 5
arr7 = np.random.randint(100,size=10)
arr7[np.argmax(arr7)] = 0
print('arr7: ')
print(arr7)

# 6
x = np.array([1,2,3,2,3,4,3,4,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])
dist = np.linalg.norm(x-y)
print('dist: ')
print(dist)

# 7
# %matplotlib notebook
np.random.seed(1)
values = np.random.randn(1000).cumsum()
fig, ax = plt.subplots()
ax.plot(values)
# plt.show()
