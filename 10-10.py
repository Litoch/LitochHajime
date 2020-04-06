import re

with open('from.txt', 'w') as f:
    f.write('Hello Mr.张，welcome you to 南京。')

with open('from.txt') as f:
    texts = f.read()

print(texts)
words = re.findall(r'\b[a-zA-Z]+\b', texts)
words.sort()
print(words)

with open('to.txt', 'w') as f:
    for i in words:
        f.writelines(i+'\n')
