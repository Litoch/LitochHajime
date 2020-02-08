all = []
with open('report.txt') as f:
    print(f.read())
    f.seek(0)
    for i in f.readlines():
        all.append(i.strip())
print(all)

# new array
total_array = []
for i in range(0, len(all)):
    total_array.append(all[i].split())
print(total_array)

# update title
total_array[0].append('总分')
total_array[0].append('平均分')
total_array[0].insert(0, '名次')

# new line
total_array.insert(1,['0', '平均'])
print('total array:\n', total_array)

# calculate scores of each student
for i in range(2,len(total_array)):
    sum = 0
    for j in range(1, len(total_array[i])):
        total_array[i][j] = int(total_array[i][j])
        sum += total_array[i][j]
    avg = float('%.1f' % (sum / (len(total_array[i]) - 1)))
    total_array[i].append(sum)
    total_array[i].append(avg)
print(total_array)

scores = total_array[2:]
print(scores)

# total avg
for i in range(1, len(scores[0])):
    sum = 0
    for j in range(0, len(scores)):
        sum += scores[j][i]
    if i != (len(scores[0]) -1):
        avg = int(sum/len(scores))
    else:
        avg = float('%.1f' % (sum/len(scores)))
    total_array[1].append(str(avg))

print(total_array[1])

# ranking & mark failed
scores.sort(key=(lambda x: x[-1]), reverse=True)
print(scores)

for i in range(0,len(scores)):
    scores[i].insert(0, str(i+1))
    for j in range(2, len(scores[i])):
        if scores[i][j] < 60:
            scores[i][j] = '不及格'
        scores[i][j] = str(scores[i][j])

print(scores)

for i in range(2, len(total_array)):
    total_array[i] = scores[i-2]
print(total_array)

result = [' '.join(list) + '\n' for list in total_array]
print(result)

with open('result.txt', 'w') as f:
    f.writelines(result)
