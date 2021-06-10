from requests import RequestException
import requests
from lxml import etree
from fake_useragent import UserAgent
from queue import Queue
from threading import Thread
import time

"""
二九小说网伏天氏小说下载
"""
class get_htmls(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.urls = Queue()# 存放获取的urls
        self.content_html = Queue() #存放解析后的htmls
        self.headers = {'User-Agent':UserAgent().random}
        self.url = 'https://www.2952.cc/b/1/1245/index.html'
        self.base_url = 'https://www.2952.cc'
        self.main_html = []

    def get_main_html(self):
        try:
            req = requests.get(self.url,headers = self.headers,timeout = 10)
            req.encoding = 'gbk'
            if req.status_code == 200:
                self.main_html.append(req.text)
                # print(self.main_html)
            else: return None
        except RequestException:
            return None
    def get_page_urls(self):
        e = etree.HTML(self.main_html[0])
        titles = e.xpath('//*[@id="list"]/div/div[2]/ul/li/a/text()')
        hrefs = e.xpath('//*[@id="list"]/div/div[2]/ul/li/a/@href')
        # print(titles,hrefs)
        for href in hrefs:
            href = self.base_url + href
            self.urls.put(href)
            self.urls.task_done()
    def prase_page_urls(self):
        while True:
            try:
                htmls = requests.get(self.urls.get(),headers = self.headers,timeout = 10)
                htmls.encoding = 'gbk'
                if htmls.status_code == 200:
                    htmls = htmls.text
                    self.content_html.put(htmls)
                    self.content_html.task_done()
                else: print('错误')
            except RequestException:
                print('错误')
    def run(self):
        while True:
            e = etree.HTML(self.content_html.get())
            content = e.xpath('//*[@id="content"]/text()')
            self.content_html.task_done()
            print(content)


if __name__ == '__main__':
    d = get_htmls()
    d.get_main_html()
    d.get_page_urls()
    d.prase_page_urls()
    d.run()
    d.start()