
import requests
import csv

url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=1cd5bce4874a9a3a5c34ff590736dec8&desktop=true&page_number=3&limit=6&action=down&after_id=11&ad_interval=-1'
headers = {'cookie':'_xsrf=5YXLlbmyvFRtR7QXecZ8zOuItI2csnvJ; _zap=19d43e7a-cbfa-4a46-bc5b-16ab692ebdb2; d_c0="AJDc0zkvShGPTlA8Dyo0tOxMYr6GEur30SI=|1589816212"; _ga=GA1.2.426368640.1589816214; capsion_ticket="2|1:0|10:1594734928|14:capsion_ticket|44:Njc2NmMzY2RhNjY4NGU1YWExOTc4NDYyYzk5Y2UzYTc=|4445c220f6280db2a87421b66eaa8ad2da4da1b69412d9863854a43ae2596a5b"; SESSIONID=CuX6oPbcuagebUKQooihPv8e2qw2OxhWR3qbjBbbjgU; JOID=UlEXB0wOfZepayrpMQrTyEq4dYQiRAPJnANzgFR8FfvKCnira1zJn_JlKOQ0Ia_PdCEOa4NYXAqKTq6hf-IoZ2k=; osd=UFkVA00MdZWtaijhMw7SykK6cYUgTAHNnQF7glB9F_PIDnmpY17NnvBtKuA1I6fNcCAMY4FcXQiCTKqgfeoqY2g=; z_c0="2|1:0|10:1594734930|4:z_c0|92:Mi4xaXhRMkFRQUFBQUFBa056VE9TOUtFU1lBQUFCZ0FsVk5VZ2Y3WHdCYmxub2NoOGRCV25WVks0ZmpWSWI4RW5jWHFn|22492c844e356fd2cb00d155db81bca720378691b8ce36898cad80b93b18fea8"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1593957156,1594543323,1594734928,1594736345; _gid=GA1.2.165822653.1595141901; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1595145768; KLBRSID=81978cf28cf03c58e07f705c156aa833|1595145782|1595140742',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

r = requests.get(url, headers = headers)
dict_A = r.json()
data = dict_A.get('data')

extracted = [['Author', 'Followers','Title', 'Vote', 'Comment']]
for i in data:
    list = []
    target = i.get('target')
    author_info = target.get('author')
    list.append(author_info.get('name'))
    list.append(author_info.get('followers_count'))
    list.append(target.get('title'))
    list.append(target.get('vote_count'))
    list.append(target.get('comment_count'))
    extracted.append(list)

print(extracted)

with open('./zhihu.csv', 'w', encoding='utf-8-sig') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(extracted)
