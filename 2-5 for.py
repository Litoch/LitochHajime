#1
sum = 0
for i in range(1,101):
    if i%3 == 0:
        sum = sum + i
print(sum)

#2
length = int(input('Enter the length: ')) + 1
width = int(input('Enter the width: ')) + 1

for i in range(1, length):
    for j in range(1, width):
        print('*', end=' ')
    print()


#3
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 9 x 1 = 9
# ...
# 9 x 9 = 81

for i in range(1, 10):
    for j in range(1, i+1):
        print('%d x %d = %d' % (i, j, i*j))

#4
nums = [23, 45, 8, 13, 50, 43, 21]

# 把 nums 里的值从前向后累加
# 当总和超过 100 时则不再继续累加

sum = 0
for n in nums:
    # 累加
    sum = sum + n
    if sum > 100:
        break
# 满足条件时跳出循环

print(sum)
