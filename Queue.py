from threading import Thread
from queue import Queue
import requests
from fake_useragent import UserAgent
from lxml import etree
from requests.exceptions import RequestException


#爬虫类
class CrawlInfo(Thread):
    def __init__(self,url_queue,html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        try:
            headers = {
                "User-Agent" : UserAgent().random
            }
            while self.url_queue.empty() == False:
                req = requests.get(self.url_queue.get(),headers = headers,timeout = 30).text
                # print(req)
                if req.status_code ==200:
                    self.html_queue.put(req)
                return None
        except RequestException:
            return None

#解析类
class ParseInfo(Thread):
    def __init__(self,html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue
    def run(self):
        while self.html_queue.empty() == False: #判断是否为空
            e = etree.HTML(self.html_queue.get())
            contents = e.xpath('')
            for content in contents:
                info = content.xpath('string(. )')#内格式化
                #print(info)

if __name__ == '__main__':
    #储存url的容器
    url_queue = Queue()
    #存储内容的容器
    html_queue  = Queue()
    base_url = ''
    for i in range(,):
        new_url = base_url.format(i)
        url_queue.put(new_url)
    #创建一个爬虫
    for i in range(,):
        crawl1 = CrawlInfo(url_queue)
        crawl1.start()
    parse = ParseInfo(html_queue)
    parse.start()