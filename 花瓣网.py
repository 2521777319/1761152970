import requests
from fake_useragent import UserAgent
from lxml import etree
# import io
# import sys
import time
from urllib.parse import quote
from random import randint

def get_htmls(headers,recreat_url):
    req = requests.get(recreat_url,headers = headers,timeout = 30)
    req.encoding = 'utf-8'
    # print(req.text)
    return req.text
def get_urls():
    pass
def parse_urls(htmls):
    e = etree.HTML(htmls)
    href = e.xpath('//div/a[@class="img x layer-view loaded"]/@href')

def get_contents():
    pass
def save():
    pass
def main():
    headers = {
        'User-Agent' : UserAgent().random
    }
    # key = quote(input('请输入想要下载哪类图片： \n'))
    official_url = 'https://huaban.com/'
    search_url = 'https://huaban.com/search/?q=%E6%91%84%E5%BD%B1'
    recreat_url = ''
    htmls = get_htmls(headers,search_url)
    time.sleep(randint(3,5))
    parse_urls(htmls)

if __name__ == '__main__':
    main()