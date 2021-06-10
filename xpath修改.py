import requests
from lxml import etree
from fake_useragent import UserAgent

headers1 = {
    'User-Agent' : UserAgent().random
}

url = 'http://www.xbiquge.la/14/14930/6753003.html'
r = requests.get(url,headers = headers1,timeout = 30)
r.encoding = "utf-8-sig"
req = r.text
res = etree.HTML(req)
# print(res)
title = res.xpath('//div[@class="bookname"]/h1/text()')[0]
print(title)
content = res.xpath('//*[@id="content"]/text()')[:]
for i in content:
    print(i)

