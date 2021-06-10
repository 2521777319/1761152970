from threading import Thread
from queue import Queue
import requests
from lxml import etree
from fake_useragent import UserAgent
from requests.exceptions import RequestException
import re
# https://www.ximalaya.com/youshengshu/2902957/p1/
#https://www.ximalaya.com/revision/play/v1/audio?id=9037805&ptype=1
class FirstCraw(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.headers = {'User-Agent':UserAgent().random}
        self.url_queue = Queue()
        self.play_url = Queue()


    def get_maxpage(self):
        """
        获取最大页数
        """
        url = 'https://www.ximalaya.com/youshengshu/2902957/'
        try:
            res = requests.get(url,headers = self.headers)
            if res.status_code == 200:
                res.encoding = 'utf-8'
                res = res.text
                e = etree.HTML(res)
                max_page = e.xpath('//*[@id="anchor_sound_list"]/div[2]/div/nav/ul/li[7]/a/span/text()')
                return max_page
                # print(max_page[0])
            else:print('请求出错')
        except RequestException:
            print("请求出错")

    def prase_url(self):
        """
        解析每一页的url
        将获取到的真实url放入队列
        """
        while True:
            res = requests.get(self.url_queue.get(),headers = self.headers)
            res.encoding = 'utf-8'
            res = res.text
            # print(res)
            href = re.findall('"url":"/youshengshu/2902957/(.*?)"',res)
            # print(href)
            for i in href:
                play_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(i)
                self.play_url.put(play_url)
    def save(self):
        count = 1
        while True:
            res = requests.get(self.play_url.get(),headers = self.headers).content
            with open('D:\喜马拉雅\%s.m4a'%count,'w') as f:
                f.write(res)
                count += 1
                print("%s已经下载完毕"%count)
    def diaoduqi(self):
        """
        获取每一页上面的url
        放入队列当中
        """
        page = self.get_maxpage()
        # print(page[0])
        for i in range(int(page[0])):
            url = 'https://www.ximalaya.com/youshengshu/2902957/p{}/'.format(i)
            self.url_queue.put(url)
        # print(self.url_queue)
        crawl_list = []
        for i in range(0, 3):
            crawl1 = self.prase_url()
            crawl_list.append(crawl1)
            crawl1.start()
        for crawl in crawl_list:
            crawl.join()
        parse_list = []
        for i in range(0, 3):
            parse = self.save()
            parse_list.append(parse)
            parse.start()
        for parse in parse_list:
            parse.join()
if __name__ == "__main__":
    R = FirstCraw()
    R.diaoduqi()
