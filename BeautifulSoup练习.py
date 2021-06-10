import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

url = 'https://movie.douban.com/'

headers = {
    'User-Agent' : UserAgent().random
}

req = requests.get(url,headers = headers,timeout = 10).text

#lxml, html5lib ,等
res = bs(req,'html5lib')

# #格式化输出
# print(res.prettify())
