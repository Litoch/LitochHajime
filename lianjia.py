import requests
import csv
from bs4 import BeautifulSoup

# head
extracted = [['Title', 'Link', 'Block', 'Area', 'Direction', 'Structure', 'Floor', 'Remarks']]

# headers
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

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
        info.append(i.p.a.get_text(strip=True))
        info.append(i.p.a.get('href'))
        details = i.find(class_="content__list--item--des").get_text(strip=True)
        for j in details.split('/'):
            info.append(j)
        remarks = i.find(class_="content__list--item--bottom oneline").get_text()
        info.append(','.join(remarks.split()))
        extracted.append(info)

with open('./lianjia.csv', 'w', encoding='utf-8-sig') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(extracted)
