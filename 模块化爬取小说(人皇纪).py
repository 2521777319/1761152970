import requests
from fake_useragent import UserAgent
from lxml import etree
import time


def get_urls(url,headers):
    req = requests.get(url,headers = headers,timeout = 30)
    req.encoding = 'utf-8'
    e = etree.HTML(req.text)
    hrefs = e.xpath('//*[@id="list"]/dl/dd/a/@href')
    return hrefs
def get_titles(url,headers):
    req = requests.get(url,headers = headers,timeout = 30)
    req.encoding = 'utf-8'
    e = etree.HTML(req.text)
    titles = e.xpath('//*[@id="list"]/dl/dd/a/text()')
    return titles

def get_content(url,headers):
    req = requests.get(url,headers = headers,timeout = 30)
    req.encoding = 'utf-8'
    e = etree.HTML(req.text)
    contents = e.xpath('//*[@id="content"]/text()')
    # for content in contents:
    return contents
def save_content():
    pass

def main():
    headers = {
        'User-Agent': UserAgent().random
    }
    url = 'http://www.xbiquge.la/10/10512/'
    urls = get_urls(url,headers)
    titles = get_titles(url,headers)
    time.sleep(5)
    # print(urls)
    # print(titles)
    for base_url in urls:
        url = 'http://www.xbiquge.la' + base_url
        # print(url)
        contents = get_content(url,headers)
        for content in contents:
            print(content)

if __name__ == '__main__':
    main()