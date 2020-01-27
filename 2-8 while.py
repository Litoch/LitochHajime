#1
from random import randint

num = randint(1,10)

while True:
    answer = int(input('Guess a number from 1 to 10: '))
    if answer < num:
        print('too small')
    elif answer > num:
        print('too big')
    else:
        print('BINGO')
        break


#2
# 输出 1 到 10，但不输出 4 和 5
count = 0
while count < 10:
    count += 1
    if count == 4 or count == 5:
        continue
    print(count)


#3
i = 0
sum = 0
while i < 100:
    i += 1
    if i%3 == 0:
        sum = sum + i

print(sum)
