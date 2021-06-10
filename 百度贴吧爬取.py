import requests
from fake_useragent import UserAgent
import time
import io
import sys
from lxml import etree
from urllib import parse

def get_urls(base_url,beginPage,endPage):
    for page in range(beginPage,endPage+1):
        pn = (page - 1) * 50
        url = base_url + "&pn=" + str(pn)
        # print(url)
        return url
def get_htmls(urls,headers):
    html = requests.get(urls,headers = headers,timeout = 30)
    html.encoding = 'utf-8'
    # print(html.text)
    return html.text
def get_content(html):
    e = etree.HTML(html)
    titles = e.xpath('//*[@class="threadlist_title pull_left j_th_tit"]/a[@rel="noreferrer"]/text()')
    for title in titles:
        print(title)
def save_content():
    pass
def main():
    kw = input("请输入需要爬取的贴吧：\n")
    beginPage = int(input("请输入起始页： \n"))
    endPage = int(input("请输入结束页： \n"))
    key = parse.urlencode({'kw' : kw})
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    headers = {
        'User-Agent' : UserAgent().random
    }
    base_url = 'https://tieba.baidu.com/f?' + key
    urls = get_urls(base_url,beginPage,endPage)
    html = get_htmls(urls,headers)
    content = get_content(html)
if __name__ == '__main__':
    main()