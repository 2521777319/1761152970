import requests
from fake_useragent import UserAgent
from lxml import etree
from requests.exceptions import RequestException
import re
import time

#多线程
from threading import Thread
from queue import Queue

class CrawInfo(Thread):
    def __init__(self,url_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
    def run(self):
        headers = {
            'User-Agent': UserAgent().random
        }
        while self.url_queue.empty() == False:
            try:
                html = requests.get(self.url_queue.get(), headers=headers, timeout=30)
                html.encoding = 'utf-8'
                time.sleep(5)
                if html.status_code == 200:
                    print(html.text)
                return None
            except RequestException:
                return None

class PraseInfo(Thread):
    def __int__(self,html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue
    def run(self):
        while self.html_queue.empty() == False:
            e = etree.HTML(self.html_queue.get())


def main():
    url_queue = Queue()
    html_queue = Queue()




if __name__ == '__main__':
    main()