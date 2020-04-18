# 一般面向过程需要多次重新定义变量
# speed = 50.0
# price = 2.5
# distance = 180
# print('time is', distance / speed)
# print('cost', distance * price)
#
# speed2 = 70.0
# price2 = 3.5
# print('time is', distance / speed2)
# print('cost', distance * price2)


# def drive(speed, price, distance):
#     print('time is', distance / speed)
#     print('cost', distance * price)
#
#
# # 尝试用字典表示一辆车的属性
# distance = 180
# car = {
#     'speed': 50.0,
#     'price': 2.5
# }
# drive(car['speed'], car['price'], distance)
#
# car2 = {
#     'speed': 70.0,
#     'price': 3.5
# }
# drive(car2['speed'], car2['price'], distance)


# 面向对象方法

# class Car:
#     speed = 50.0
#     price = 2.5

#     def drive(self, distance):
#         print('time is', distance / self.speed)
#         print('cost', distance * self.price)


# c1 = Car()
# c1.drive(180)

# # 可以修改对象属性
# # 只修改部分属性，剩余保持默认
# c2 = Car()
# c2.speed = 70.0
# c2.price = 3.5
# c2.drive(180)


class Car:
    # def __init__(self):     # 一个对象被创建的时候调用, 可提供额外参数
    #     # 通常把属性的初始化工作放在init中进行
    #     print('init a Car')
    #     self.speed = 50.0
    #     self.price = 2.5

    def __init__(self, sp=50.0, pr=2.5):     # 一个对象被创建的时候调用, 可提供额外参数
        # 通常把属性的初始化工作放在init中进行
        print('init a Car')
        self.speed = sp
        self.price = pr
        self.distance = 0

    def drive(self, distance):
        self.distance += distance
        print('total drive', self.distance)
        # 不加self为函数局部变量
        # 加了以后为这辆Car的distance属性
        # 一个对象的属性跟随该对象
        # 如果在某个方法中被修改了，再次访问该属性就是被修改过的值
        print('time is', distance / self.speed)
        print('cost', distance * self.price)
        print()     # 输入换行

c1 = Car()
c1.drive(180)
c1.drive(50)
c1.drive(90)
