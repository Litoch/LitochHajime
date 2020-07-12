import requests

url = 'https://weibo.com/a/hot/realtime'
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
           'cookie':'Ugrow-G0=6fd5dedc9d0f894fec342d051b79679e; SUB=_2AkMoVkBZf8NxqwJRmfsRyWLqb4p2yQ_EieKeCrGCJRMxHRl-yT9kqlQttRB6A9ZutqzkcB_aszLkZ2WjLNYPG1upKnDX; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh8EcNmN2QE7mjuP8G40I_4; YF-V5-G0=f5a079faba115a1547149ae0d48383dc; WBStorage=42212210b087ca50|undefined'}

r = requests.get(url, headers = headers)
with open('./weibohot.html', 'w') as f:
    f.write(r.text)
