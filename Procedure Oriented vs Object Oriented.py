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

class Car:
    speed = 50.0
    price = 2.5

    def drive(self, distance):
        print('time is', distance / self.speed)
        print('cost', distance * self.price)


c1 = Car()
c1.drive(180)

# 可以修改对象属性
# 只修改部分属性，剩余保持默认
c2 = Car()
c2.speed = 70.0
c2.price = 3.5
c2.drive(180)
