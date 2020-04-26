from random import randint
import requests

# times = 0
# total_round = 0
# total_times = 0
#
# while True:
#     main_menu = input("1.Start  2.Quit\n")
#     # name = input("Please enter your name: ")
#     if main_menu == '1':
#         times = 0
#         total_round += 1
#         while True:
#             times += 1
#             answer = int(input('Enter a number: '))
#             if answer < num:
#                 print('too small')
#             elif answer > num:
#                 print('too big')
#             else:
#                 print('BINGO!')
#                 total_times = total_times + times
#                 print('You have guessed %d times this round!' % times)
#                 print('You have played %d round!' % total_round)
#                 print('The average times you guess in one round is %.2f' % (total_times/total_round))
#                 break
#     if main_menu == '2':
#         print('See you next time')
#         break


# function version




from random import randint

def guess(num):
    while True:
        ans = int(input('Guess a integer within 10: '))
        if ans > num:
            print('too big')
            return False
        elif ans < num:
            print('too small')
            return False
        else:
            print('BINGO!')
            return True

# 指定数字
# def play(num=0):
#     if num == 0:
#         num =randint(1,10)
#     while not guess(num):
#         pass

def play():
    global times
    times = 0
    # avg_times = total_times / total_round
    r = requests.get('https://python666.cn/cls/number/guess/')
    num = int(r.text)
    while not guess(num):
        times += 1
        pass


total_round = 0
total_times = 0
while True:
    choice = input('1.Start  2.Quit')
    if choice == '1':
        total_round += 1
        play()
        total_times += total_times + times
    if choice == '2':
        print('See you next time')
        break
    #  其他输入没有影响，重复while True的循环也就是提示choice的input
