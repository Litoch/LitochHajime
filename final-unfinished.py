import requests


def CheckInput():
    global ans
    try:
        ans = int(input('Guess an number within 100: '))
    except:
        print('Please enter a number')
        return False
    else:
        return True


def guess(num):
    while True:
        while not CheckInput():
            pass
        if ans > num:
            print('too big')
            return False
        elif ans < num:
            print('too small')
            return False
        else:
            print('BINGO!')
            return True


def play():
    global times
    times = 1
    r = requests.get('https://python666.cn/cls/number/guess/')
    num = int(r.text)
    while not guess(num):
        times += 1
        pass


total_round = 0
total_times = 0
times_list = []
name = input('Please enter your name: ')


while True:
    total_round += 1
    play()
    times_list.append(times)
    total_times += total_times + times
    choice = input('Do you want to play again? Press Y to continue. Else to quit.')
    if choice == 'Y' or choice == 'y':
        pass
    else:
        print('\nSee you next time')
        break
    #  其他输入没有影响，重复while True的循环也就是提示choice的input


avg_times = total_times/total_round
min_this_round = min(times_list)
print('\n%s, you have played %d rounds.\n'
      ' The fastest round ended with %d times.\n'
      'The average times you guess in one round is %.2f'
      % (name, total_round, min(times_list), avg_times))
score = [name, str(total_round), str(min_this_round), str(avg_times)]


records = []
try:
    with open('game record.txt') as f:
        for i in f.readlines():
            records.append(i.strip())
except:
    with open('game record.txt', 'w') as f:
        pass


# print('After read the file: ')
# print(records)


detailed_records = []
for i in range(0, len(records)):
    detailed_records.append(records[i].split())


# print('After split:')
# print(detailed_records)


# update the existent records
TF_list = []
for i in range(0, len(records)):
    last_total_round = int(detailed_records[i][1])
    last_avg_times = float(detailed_records[i][3])
    last_total_times = last_total_round * last_avg_times
    if detailed_records[i][0] == name:
        detailed_records[i][1] = str(last_total_round + total_round)
        if int(detailed_records[i][2]) > min_this_round:
            detailed_records[i][2] = str(min_this_round)
        detailed_records[i][3] = str((last_total_times + total_times) / (last_total_round + total_round))
        TF_list.append(True)
    else:
        TF_list.append(False)


if True not in TF_list:
    detailed_records.append(score)


# print('\nfinal detailed records: ')
# print(detailed_records)


final_records = [' '.join(line) + '\n' for line in detailed_records]
# print('\nfinal records')
# print(final_records)


with open('game record.txt', 'w') as f:
    for i in final_records:
        f.writelines(i)

