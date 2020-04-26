# 无需换行
print('hello', end="")

# terminal python命令对大小写敏感
# 查看版本  python -V

# get path
# command + option + c


num = 18
print('price is %d' % num)
print('price is %f' % 4.99)
print('price is %s' % 'free')

print('price is %f' % 4.99)	#4.990000
print('price is %.2f' % 4.99)	#4.99 
print('price is %.2f' % 4.998)	#5.00
print('%s got a score of %d' % ('A', 87))	#tuple
print('{} is a {}'.format(A, gay))	#无需制定变量类型
#f-string
name = 'Lily'
score = 95
print(f'{name} is {score}')

# print 三角 *
for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end=' ')
    print()

# 生成随机数
# random
# import random
# num = random.randint(1, 100)
from random import randint
num = randint(1, 100)
print(num) 

# 猜数字游戏
# guess number game

random.random()		# 生成一个0～1之间的随机小数
random.choice([1, 3, 5])	# 从1、3、5之中随机挑选一个值
# 查看random中有哪些函数和变量
dir(random)

from math import pi as math_pi
print(math_pi)


# 全局变量 global
# 局部变量 local
def sayHello():
	global age
	age += 1
	print('you are', age)

age = 18
sayHello()
print('your age is', age)

output:
you are 19
your age is 19

# 变量前加* -- 调用时的参数会存储在一个tuple对象中
def calcSum(*args): 
    sum = 0
    for i in args:
        sum += i
    print(sum)

calcSum(3,6,20)

# func(**kargs) --  参数以键值对字典的形式传入
def printAll(**kargs):
	for k in kargs:
		print(k, ':', kargs[k])
printAll(a=1, b=2, c=3)

output:
a : 1
b : 2
c : 3

# 带有默认值的形参(arg=)须在无默认值的形参(arg)后之后：default argument follows non-default argument
# tuple参数(*args)须在带有默认值的形参(arg=)之后
# dictionary参数(**kargs)须在tuple参数(*arg)之后

# 按顺序把无指定参数的实参赋值给形参；
# 把指定参数名称(arg=v)的实参赋值给对应的形参；
# 将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
# 将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。

# lambda表达式
sum = lambda a, b, c: a + b + c
print(sum(1, 2 ,3))

def sum(a, b, c):
	return a + b + c
print(sum(1, 2, 3,))

# funtion + lambda
def fn(x):
	return lambda y: x + y

a = fn(2)
print(a(3))


arr = [365, 'everyday', 0.618, True]
arr.index('everyday')
>>> arr.index('everyday')
1
>>> arr.index(True)
3

>>> arr.append(2)
>>> arr
[365, 'everyday', 0.618, True, 2]

>>> arr.insert(1, 'aaa')
>>> arr
[365, 'aaa', 'everyday', 0.618, True, 2]

>>> arr = [365, 'everyday', 0.618, True]
>>> arr2 = [2, 'aaa']
>>> arr + arr2
[365, 'everyday', 0.618, True, 2, 'aaa']

>>> arr.remove('everyday')		# 如果要删除的元素有多个，只删除最前面那一个
>>> arr
[365, 0.618, True]



>>> arr.pop(2)		# del arr[2]
True
>>> arr
[365, 0.618]

# 修改
>>> arr[0] = 300
>>> arr
[300, 0.618]

arr.sort(reverse=True)


# list comprehension/列表解析：通过已有列表生成新列表
print([i for i in arr])
[i for i in arr if i > 3]
[i*2 for i in arr if i > 3]

arr2=[]
for i in arr:
	if i > 3 :
		arr2.append(i*2)

# list排序
arr.sort(reverse=True)		#改变原列表，没有返回值
sorted(arr, reverse=True)	#不改变原列表，有返回值

l = [[1, '学'], [3, '使'], [5, '快'], [2, '习'], [4, '我'], [6, '乐']]
print(sorted(l, key=lambda x: x[0]))

a = 'a b c'
l = a.split()
print(l)
b = ' '.join(l)
print(b)
c = ' '
print(c.join(l))


# 把1到100的整数里，能被2，3，5同时整除的数取出
# 以分号(;)分隔的形式输出

#1
result = []
for i in range(1, 101):
    if i%2==0 and i%3==0 and i%5==0:
        result.append(str(i))
print(result)
print(";".join(result))

#2
print(';'.join([str(i) for i in range(1,101) if i%2==0 and i%3==0 and i%5==0]))


# dict: key-value
dict1 = {key1:value1, key2:value2}
# key:string, integer, float
# value: any
# 遍历字典
目录
for k in price:
    print(k, price[k])
del price['galaxy']
print('mi' in price)	# True

price.kyes()
price.values()
price.get('iphone')


# 集合(set) -- 不常用到
set1 = {1,2,3}
set2 = {3,4,5}
# 并集
print(set1 | set2)
# 交集
print(set1 & set2)
# 异域
print(set1 ^ set2)
# 补集
print(set1 - set2)

# 集合补允许出现重复的元素，可以利用该性质来去除列表中的重复元素
arr = [1,1,1,3,3,5,7,7]
s = set(arr)
print(s)
arr_n = list(s)
print(arr_n)


random.randrange(start=0, stop, step=1)		# not including stop. 
random.sample(population, k)
random.shuggle(x)

math.pi
math.e

math.ceil(x)
math.floor(x)
math.pow(x,y)
math.log(b, a=e)
math.sqrt()
math.fabs()

# 三角函数以弧度为单位
math.degree(x)		# 弧度转角度
math.radians(X)		# 角度转弧度


f = open('/Users/litoch/test.txt')
content = f.read()

print(content)
f.close()

read: 读取整个
readline：一次读一行
readlines：一次读完这个歌文件，每行作为一个元素存入列表中
>>> multi_lines_file.readlines()
['python\n', 'python2\n', 'python3']




# 相对路径
# 文件与程序在同一个目录
python.txt
# 文件在程序当前目录下的子文件夹内，可省略共同的路径部分
another_dir/crossin.txt
# 如果文件在当前目录的上级目录内
../aaa.txt
# 反斜杠不转义（win默认路径）
r'd:\test\temporary\python.txt'

# 一次性读取方案
with open('/Users/litoch/test.txt') as f:
    print(f.read())

# 读取只能一次，再次读取前需要将文件指针移动至文件开头
f.read()
f.seek(0)
f.read()

with open('/Users/litoch/test.txt', 'w') as f:
	pass

with open('/Users/litoch/test.txt', 'w') as f:
	f.write('hello write file.')
#一旦写入文件会被清空

with open('/Users/litoch/test.txt', 'a') as f:
	f.write('hello write file.')
#无法读取可以在文件末尾写入

with open('/Users/litoch/test.txt', 'r+') as f:
    print(f.read())
    f.write('world')
# 兼顾读取和写入

txt = ['line1\n', 'line2\n','line3']
with open('/Users/litoch/test.txt', 'w') as f:
	f.writelines(txt)
#不可以连续读取但可以连续写入，写入位置在文件末尾

with open('/Users/litoch/test.txt') as fin:
    lines = fin.readlines()
    print(lines)
    i = 0
    for line in lines:
    	print(line)
    	i += 1
    	filename = '/Users/litoch/out_%d. txt' % i
    	with open(filename, 'w') as fout:
    		four.write(line)
#读取一个文件内容分别写入三个文件


try:
	with open('xxx.txt') as f:
		print(f.read())
except IOError:
	print('io error')
except: 	# 让最后一个except处理其他类型的error
	print('error')
# 得到捕获的异常
# except IOError as e_io:
# 	print('io error', e_io)
# except Exception as e:
# 	print('error', e)
else:
	print('success')
finally:	#收尾工作防止其他误操作
	


# ErrorType
FileNotFoundError
ValueError
ModuleNotFoundError
IndexError
NameError
SyntaxError
IndentationError
TypeError
ZeroDivisionError
IOError


# py3内部str字符串的unicode值无法直接传输，必须encode城字节bytes类型
>>> s = '你好'
>>> s.encode('utf8')
b'\xe4\xbd\xa0\xe5\xa5\xbd'
>>> s.encode('gbk')
b'\xc4\xe3\xba\xc3'
# 带b的就是bytes类型
>>> b = b'\xe4\xbd\xa0\xe5\xa5\xbd'
>>> b.decode()
'你好'
>>> b.decode('gbk')
'浣犲ソ'
# encode/decode不加参数会使用系统的默认编码
# 通常解码和编码过程是python自动完成的


# 爬虫
r = requests.get('http://httpbin.org/get')

print(r.text)         # 返回的文本内容
print(r.status_code)  # 请求返回状态码
print(r.encoding)     # 返回内容的编码

# 下载图片
req = requests.get('http://www.baidu.com')
req.encoding = 'utf8'
text = req.text
print(text)

# JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
# JSON 是轻量级的文本数据交换格式
# JSON 独立于语言 *
# JSON 具有自我描述性，更易理解
# 可以通过json方法直接转为字典
r = requests.get('http://httpbin.org/get')
data = r.json()
print(type(data), data)

# post -- 模拟网页上提交表单的操作
url = 'http://httpbin.org/post'
data = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=data)
print(r.text)

# HTTP状态码(HTTP Status Code)
# 浏览器访问网页时，会向网页所在服务器发出请求。服务器会返回一个包含HTTP状态码
# 的信息头(server header)用以响应浏览器的请求
[常见状态码]
200 - 请求成功
301 - 资源（网页等）被永久转移到其他URL
404 - 请求的资源（网页等）不存在
500 - 内部服务器错误

[状态码分类]
1** 信息，服务器收到请求，需要请求者继续执行操作
2** 成功，操作被成功接收并处理
3** 重定向，需要进一步的操作以完成请求
4** 客户端错误，请求包含错误语法或无法完成请求
5** 服务器错误，服务器在处理请求的过程中发生了错误


r = requests.get('http://www.baidu.com')
print(r)
>>> <Response [200]>
print(req.status_code)
>>> 200


# cookie信息：用来标记用户身份
# 浏览器给服务器的请求会带上一个请求头，包含：请求的来源、浏览器版本、支持的语言/格式/编码/压缩模式，cookie
# 以此信息来判断一个请求是否为真实用户请求
# ↑因此经常需要加上必要信息才可成功请求
常见headers参数：
Cookie 		记录用户身份的信息					Cookie:$Version=1;Skin=new;
													version=1;sessionid=12345678;
Host		制定请求的服务器的域名和端口号		Host:www.crossincode.com
												 www.test.com
Referer		先前网页的地址，即请求来路地址		Referer:http://www.crossincode.com/home/
													http://www.test.com//index.html
User-Agent	浏览器信息						User-Agent: Mozilla/5.0(Linux;X11)


加上headers信息：
url = 'http://httpbin.org/get'
h = {
    'host': 'httpbin.org',
    'user-agent': 'chrome v70',
    'cookie': 'id=123;some_cookie_info'  # 非真实数据
}
r = requests.get(url, headers=h)
print(r.text)


做爬虫时，需要多次请求保持cookie一致，比如登陆后才可访问的页面。可用Session会话对象实现
s = requests.Session()
r1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
print(r1.text)
r2 = s.get("http://httpbin.org/cookies")
print(r2.text)


SSL/HTTPS证书无效导致无法访问时：
r = requests.get('https://www.12306.cn/', verify=False)
print(r.text)


r = requests.get('http://www.baidu.com')
print(r.text)
# output中含：<title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é -- requests没有拿到正确网页编码
print(r.encoding)
# ISO-8859-1：没判断出网页编码的默认值

r.encoding = 'utf8'
print(r.text)
# <title>百度一下，你就知道

if r.status_code == requests.codes.ok:
    print('success')


# 在网页右键 检查（F12）-network-刷新-discover
#
url = 'http://xueqiu.com/p/discover'
req_headers = {
    'User-Agent': 'Chrome',
    'Host': 'xueqiu.com',
    'Referer': 'http://xueqiu.com',
    'Cookie': 'aliyungf_tc=AQAAAA6LxyGldQUAIwnccvYrrwYALqY/; acw_tc=2760821e15814181563728040e24b766b4b31547b09426432393d3aa3cba2f; s=d0137ww85n; xq_a_token=b2f87b997a1558e1023f18af36cab23af8d202ea; xq_r_token=823123c3118be244b35589176a5974c844687d5e; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4MzE0MzIwMCwiY3RtIjoxNTgxNDE4MTMxMDkwLCJjaWQiOiJkOWQwbjRBWnVwIn0.aNbeesYW3qXWyqJS0GZzB-8-3H2c3S5obI1aOnFfEuEMTxt7tVpUf_c2D6IHcTjESeWkvuN_3AOrsEcKsRbZEJuKMySryVJF_spU_ors8URxNqhXnvtpm06xmhk4ZzxyGqHV3bagDLG_0sXYUgqQKMEf3t6p4RnIUpsk2CuAgpCjsP1se4n54ab5sZ_ElKvk9avLw3IM2CTZTg5SSf02GrxRVj_F7uQ9An6tISMipiZx-SaHIdykJH0qnIGmRp79QeV1RlWCZ0UUA1kO7Rc4ZmBYQtDhI7AQlQ9jdGTt-bcOChTnsWifr5-Wy5BOOV7z74pL_C3qrBz6b66uLsoZ1g; u=311581418157087; device_id=b8c2c31268ba543d6d40188bc62113be; Hm_lvt_1db88642e346389874251b5a1eded6e3=1581418158; __utmc=1; __utmz=1.1581418158.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=1.1527836471.1581418158.1581418158.1581420127.2; __utmt=1; __utmb=1.1.10.1581420127; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1581420127'
}
req = requests.get(url, headers = req_headers)
print(req.text)


# 墙外
url = 'http://www.google.com'
try:
    req = requests.get(url, timeout = 1)
    print(req.text)
except:
    print('timeout')


# 正则表达式 -- 描述文本规则的代码
# 非python特有功能，是一种通用方法
# python中正则表达式库，利用正则表达式来搜索文本
# 要使用它，你必须会自己用正则表达式来描述文本规则
'\d' - 匹配数字
'\s' - 匹配空白符
'.'  - 匹配除换行符以外的任意字符
[]   - （中括号里加上字符）匹配这其中的任意一个字符
'+'表示至少一个字符，'?'表示0或1个字符，'*'表示任意数量连续字符（包括0个）
'{n}'表示n个字符，'{n,m}'表示n～m个字符
'^'匹配整个字符串的开始，'$'匹配整个字符串的结束


# 正则模块 -- re
import re
text = 'Hi, I am Shirlet Hilton. I am his wife.'
m = re.findall(r'hi', text)
if m:
	print(m)
else:
	print('not mach')

>>> ['hi', 'hi']


m = re.search(r'hi', text)
if m:
	print(m)
else:
	print('not mach')
>>> <_sre.SRE_Match object; span=(10, 12), match='hi'>


m = re.match(r'\d{11}', '13913812345')
if m:
    print(m.group())


m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# ^ -- 匹配字符串的开始位置       $ -- 匹配字符串的结尾位置
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 贪婪匹配，匹配尽可能多的字符
r - re.search(r'10+', 1000000)
print(r.group())
# +? -- 非贪婪匹配，尽可能少匹配=一旦匹配成功就停止
r = re.search(r'10+?', 1000000)
print(r.group())


rule = re.compile(r'\d{3}-\d{3,8}')
tests = ['010-12345', '025-45678', '+86-1319999','021-8888', '020-1234567']
for t in tests:
    m = rule.match(t)
    if m:
        print(m.group())
    else:
        print('not match')
>>> 
010-12345
025-45678
不匹配
021-8888
020-1234567


text = "Hi, I am Shirley Hilton 123. I am his wife. 456"

# 取出 text 中所有连续的数字
regex = r'\d+'
m = re.findall(regex, text)
print(m)

# 取出 text 中所有的单词（不包括数字）
regex = r'\b[a-zA-Z]+\b'
n = re.findall(regex, text)
print(n)


正则表达式汇总：
Hi, I am Shirley Hilton. I am his wife.

'''
r'hi': r = raw，对字符串不进行转义

\b -- 表示单词的开头或结尾，不匹配任何字符，代表的只是一个位置
[Hh] -- H or h
[a-zA-Z] -- 全字母
[^a] -- [a]的反义
[^abcd] -- 除abcd以外的任意字符

[0-9] -- 全数字
\d -- 数字
任意长度数字（包括长度为0的空字符）：
[0-9]*
\d*
任意长度数字（1个或更长）：
[0-9]+
\d+
11位的数字：
\d{11}
第一位数为1的11位数字（比如手机号）：
1\d{10}

? -- 重复0次或1次
{n,} -- 重复n次或更多次
{n,m} -- 重复n到m次

表示一段4到12位的字符，包括字母或数字或下划线或汉字（可以作为用户注册时检测用户名的规则）：
^\w{4,12}$
表示15到18位的数字，可以用来检测身份证号码：
\d{15,18}
以1开头的一串数字，数字结尾有字母x，也可以没有。有的话就带上x：
^1\d*x?

\w -- 匹配字母或数字或下划线或汉字
\s -- 匹配任意空白符
^ -- 匹配字符串的开始
$ -- 匹配字符串的结束

\W -- 匹配任意不是字母、数字、下划线、淮南子的字符
\D -- 匹配任意非数字的字符
\B -- 匹配不是单词开头或结束的位置

. -- 换行符以外的任意字符
\S -- 空白符意外的任意字符
* -- 表示数量：前面的字符可以重复任意多次（包括0次）

r'I.*e' = 贪婪匹配
>>> ['I am Shirley Hilton. I am his wife']
r'I.*?e' = 懒惰匹配
>>> ['I am Shirle', 'I am his wife']

需要用到.或*等符号本身：，加转义字符：
\d+\.\d+

'''

'''
面向对象 ———— 程序设计方法：把数据和对数据的操作用“对象”包裹起来 

类（class）：一种抽象的类型
对象（object）：类型的具体实例

Objects are an encapsulation of variables and functions into a single entity. 
Objects get their variables and functions from classes.
Classes are essentially a template to create your objects.

“笔”作为一个抽象的概念，可以被看成是一个类
而一支实实在在的笔，则是“笔”这种类型的对象

属于一个类的函数 ———— 类的方法
属于一个类/对象的变量 ———— 属性

'''


# 用内置的dir()可以查看一个类或者实例的所有属性和方法
s = 'hello'	# 定义一个str类型的对象
print(dir(s))

str -- 类
s -- str（类型）的对象，也是一个实例


class MyClass:      # 定义一个自己的类
    pass            # 暂时内部没有内容，用pass替代

mc = MyClass()
print(mc)

>>>
<__main__.MyClass object at 0x10f35ae48>



class MyClass:  # 定义一个自己的类
    name = 'Sam'  # name为属性，'Sam'为值

    def sayHi(self):  # sayHi为方法
        # 参数self，定义类中方法的必要参数，表示方法的调用者，此处为mc这个实例
        # 不必在括号中再传入mc，默认赋值给self
        # 即self.name = mc.name      >>> 'Lily'
        print('Hello %s' % self.name)


mc = MyClass()
# 调用类中属性：对象.变量名 （没有括号！）
print(mc.name)
mc.name = 'Lily'
# 调用类中方法：对象.方法名() （有括号！）
mc.sayHi()



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

'''

Inheritance:
Inheritance allows us to define a class that inherits all the methods
and properties from another class.
Vehicle -- Parent class/Base class 基本类、超类、父类
Car/Bike -- Child class/Derived class 导出类、子类

每个子类都拥有父类的属性和方法，并可以分别添加各自独有的功能

'''


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('Spent %f hour(s)' % (distance / self.speed))

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('Consumed %f fuel' % (distance * self.fuel))

b = Bike(15.0)
c = Car(80.0, 0.012)
b.drive(100.0)
c.drive(100.0)





















