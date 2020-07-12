import requests
import time
import csv


#1
req = requests.get('https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a'
                   , headers={'User-Agent': 'Chrome'})
dict_shawshank = req.json()
# print(dict_shawshank)

image_link = dict_shawshank.get('image')
image_req = requests.get(image_link)
image = image_req.content
with open('./shawshank.png', 'wb') as f:
    f.write(image)


#2
start = 0
extracted = [['ID', 'Title', 'Rating', 'Casts', 'Poster']]
while start < 250:
    time.sleep(1)
    req = requests.get('https://api.douban.com/v2/movie/top250?start=%d&apikey=0df993c66c0c636e29ecbb5344252a4a' % start,
        headers={'User-Agent': 'chrome'})
    dict_A = req.json()
    total_info = dict_A.get('subjects')

    for i in total_info:
        list = []
        list.append(i['id'])
        list.append(i['title'])
        list.append(i['rating']['average'])
        casts_name = []
        for j in i['casts']:
            casts_name.append(j['name'])
        casts_name = ','.join(casts_name)
        list.append(casts_name)
        list.append(i['images']['small'])
        image_link = i['images']['small']
        image_req = requests.get(image_link)
        image = image_req.content
        with open('./images/%s.png' % i['title'], 'wb') as f:
            f.write(image)
        extracted.append(list)

    start += 20

print(extracted)

with open('./top250.csv', 'w', encoding='utf-8-sig') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(extracted)
