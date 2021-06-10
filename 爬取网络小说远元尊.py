# -*- coding: utf-8 -*-
import urllib.request
import bs4
import re
from lxml import etree

url = 'http://www.baidu.com/'
# 模拟浏览器访问url并获取页面内容（即爬取源码）
#def getHtml(url):
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
date = etree.HTML(html)
print(date)






