#1
# 创建一个字典，包含 one、two、three 三个键
# 对应的值分别为 1，2，3
data = {
    'one':1,
    'two':2,
    'three':3
}

# 将 two 键对应的值改为 4
data['two'] = 4

print(data)

#2
para = 'Beautiful is better than ugly ' \
      'Explicit is better than implicit ' \
      'Simple is better than complex ' \
      'Complex is better than complicated ' \
      'Flat is better than nested ' \
      'Sparse is better than dense'

wordlist = para.split()
dict_count={}

for i in wordlist:
    dict_count[i]=''

for k in dict_count:
    count = 0
    for j in wordlist:
        if k == j:
            count += 1
    dict_count[k] = count
    print('%s:  %d' % (k, dict_count[k]))
