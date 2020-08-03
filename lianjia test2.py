import requests
import csv
from bs4 import BeautifulSoup
import re

# head
extracted = [['Title', 'Link', 'Block', 'Area', 'Direction', 'Structure', 'Floor', 'Remarks']]

# headers
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

gettitle = re.compile(r'<a.*?>(.*?)</a>',re.S)
getlink = re.compile(r'<a href="(.*?)" target="_blank">',re.S)
getblock = re.compile(r'<a.*?>(.*?)</a>')
getarea = re.compile(r'(\d*㎡)',re.S)
getdir = re.compile(r'</i>([东南西北]+.*?) *<i>',re.S)
getstrc = re.compile(r'\d室\d厅\d卫',re.S)
getfloor = re.compile(r'.楼层',re.S)

for page in range(1,6):
    url = 'https://sh.lianjia.com/zufang/pg%d/#contentlist' % page
    try:
        r = requests.get(url,headers=headers)
    except:
        print('Requests Error')

    html_lianjia = r.text
    soup = BeautifulSoup(html_lianjia, 'html.parser')

    maincontent = soup.find_all(class_='content__list--item--main')

    for i in maincontent:
        info = []
        title = re.findall(gettitle,str(i))[0]
        title = re.sub('\n','',title)
        title = re.sub(' ','',title)
        info.append(title)

        link = re.findall(getlink,str(i))[0]
        info.append(link)

        des = i.find(class_="content__list--item--des")
        block = re.findall(getblock,str(des))
        if len(block)!=0:
            block = '-'.join(block)
            info.append(block)
        else:
            info.append('/')

        area = re.findall(getarea,str(des))
        if len(area)!=0:
            info.append(area[0])
        else:
            info.append('/')

        direction = re.findall(getdir,str(des))
        # print(direction)
        if len(direction)!=0:
            info.append(direction[0])
        else:
            info.append('/')


        structure = re.findall(getstrc,str(des))
        if len(structure)!=0:
            info.append(structure[0])
        else:
            info.append('/')

        floor = re.findall(getfloor,str(des))
        if len(floor)!=0:
            info.append(floor[0])
        else:
            info.append('/')

        remarks = i.find(class_="content__list--item--bottom oneline").get_text()
        remarks = ','.join(remarks.split())
        info.append(remarks)
        extracted.append(info)

with open('./lianjia2.csv', 'w', encoding='utf-8-sig',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(extracted)
