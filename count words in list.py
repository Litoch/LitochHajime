list_s = ['Beautiful', 'is', 'better', 'than',
          'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']

counts = {}

for i in list_s:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1

print(counts)
