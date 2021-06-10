import requests
from fake_useragent import UserAgent
from lxml import etree
import time
from random import randint
from urllib.parse import urlencode
import re
import json
#//*[@id="play_1"]/ul/li[1]/a
base_url = 'http://v.dxsbb.com/dianqi/317/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
# headers = urlencode(headers)
req = requests.get(base_url,headers = headers,timeout = 30)
req.encoding = 'utf=8'
req = req.text
time.sleep(randint(3,6))
e = etree.HTML(req)
titles = e.xpath('//div[@id="play_1"]/ul/li/a/@title')
base_hrefs = e.xpath('//div[@id="play_1"]/ul/li/a/@href')
for title,base_href in zip(titles,base_hrefs):
    href = 'http://v.dxsbb.com' + base_href
    # print(title,href)
    response = requests.get(href,headers= headers ,timeout = 30)
    response.encoding = 'utf-8'
    response = response.text
    time.sleep(randint(3, 6))
    # print(response)
    #<iframe height=550 width=698 src='(.*?)' frameborder=0 'allowfullscreen'></iframe>
    play_url = re.findall("<iframe.*?src='(.*?)' frameborder=0 'allowfullscreen'></iframe>", response)[0]
    true_url = 'http:' + play_url
    # html = requests.get(true_url,headers = headers ,timeout = 30).content
    # time.sleep(randint(3, 6))
    info = {
        title : true_url
    }
    print(info)
    # print('正在写入：%s...'%title)
    # with open(r'D:\Users\asus\Desktop\模电\%s.txt'%title,'a+') as f:
    #     f.write(json.dumps(info))
    #     print('写入完毕：%s'%title)
#优酷json数据网址加密，视频分解，以上只获得视频地址和名称
