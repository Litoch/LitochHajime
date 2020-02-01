# create keywords file
assigned_words = ['abc\n', '测试\n', '啊啊啊\n', 'tttt']

with open('keywords.txt', 'w') as f:
    f.writelines(assigned_words)

# read and load keywords

keywords = []
with open('keywords.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        keywords.append(line)

print(keywords)

def filter(userwords = '', replacement = '*'):
    for word in keywords:
        userwords = userwords.replace(word, replacement * len(word))
    return userwords

text = input('Enter your words: ')
print(filter(text))
