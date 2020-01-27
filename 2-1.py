#1
money = 88

# 当 money 的值大于 100 时，输出 "rich"
# 否则，输出 "poor"

if money > 100:
    print("rich")
else:
    print("poor")


#2(a)
bingo = False
if bingo == False:
    print(True)
else:
    print(False)
# A: True


#2(b)
b = 3
if b - 3:
    print(True)
else:
    print(False)
# A: False

#2(c)
x = input('请输入内容')
if x:
    print(True)
else:
    print(False)
# A: if enter: False, else: True

#2(d)
a = True
b = not a
print(b)        # False
print(not b)    # True
print(a == b)   # False
print(a != b)   # True
print(a and b)  # False
print(a or b)   # True
print(1<2 and b==True)  # False


#3
h = float(input("please enter your height: "))
w = float(input("please enter your weight: "))
BMI = w / (h * h)
if BMI < 18.5:
    print(BMI, "体重偏轻")
elif (BMI >= 18.5) and (BMI<24):
    print(BMI, "体重正常")
else:
    print(BMI, "体重偏重")
