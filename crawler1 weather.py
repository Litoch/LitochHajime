import requests

while True:
    city = input('Please enter the name of CITY, ENTER to quit: \n')
    if not city:
        break
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    # print(req.text)
    dic_city = req.json()   # 将请求得到的json格式的字符串直接转成一个真正的字典
    # print(dic_city)
    # print(type(req.text))
    # print(type(req.json()))
    city_data = dic_city.get('data') # 取出data部分，后面还有'status'、'desc'部分
    if city_data:
        city_forecast = city_data['forecast'][0]
        # city_data['forecast'] -- 取出forecast部分，即去掉yesterday从今天开始
        # city_data['forecast'][0] -- 只要今天的不需要之后的
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('Fail to access')


# -------------------------- test part -------------------------------
# req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
# dic_city = req.json()   # 将请求得到的json格式的字符串直接转成一个真正的字典
# print(dic_city)
# city_data = dic_city.get('data')
# print(city_data)
# print(city_data['forecast'])
# print(city_data['forecast'][0])

# 2020.11 update
while True:
    city = input('Please enter the name of CITY, ENTER to quit: \n')
    if not city:
        print('ByeBye :)')
        break
    try:
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
        dic_city = r.json()
    except:
        print('Fail to access.')

    try:
        forecast = dic_city['data']['forecast'][0]
        print(forecast.get('date'))
        print(forecast.get('high'))
        print(forecast.get('low'))
        print(forecast.get('type'))
    except:
        print('No such CITY.')
