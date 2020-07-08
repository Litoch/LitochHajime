import requests

req = requests.get('https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a'
                   , headers={'User-Agent': 'Chrome'})
dict_shawshank = req.json()
# print(dict_shawshank)

image_link = dict_shawshank.get('image')
image_req = requests.get(image_link)
image = image_req.content
with open('./shawshank.png', 'wb') as f:
    f.write(image)
