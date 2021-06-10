import requests
import jsonpath
from queue import Queue
import threading
import time
from urllib import request

class Producer(threading.Thread):
    def __init__(self,page_queue,data_queue,*args,**kwargs):
        super(Producer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse(url)

    def parse(self,url):
        response = requests.get(url, headers=self.headers).json()
        titles = jsonpath.jsonpath(response, "$..'title'")  # 标题
        trackId = jsonpath.jsonpath(response, "$..'trackId'")  # id
        for id_, title in zip(trackId, titles):
            title = title+'.m4a'
            video_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(id_)
            resp = requests.get(video_url, headers=self.headers).json()
            src = jsonpath.jsonpath(resp, "$..'src'")[0]
            # print(src)#很多数据
            time.sleep(0.3)
            self.data_queue.put((title,src)) # 压包

class Consumer(threading.Thread):
    def __init__(self,page_queue,data_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.data_queue = data_queue
    def run(self):
        while True:
            if self.page_queue.empty() and self.data_queue.empty():
                break
            title,src = self.data_queue.get() #解包
            print(title,"下载成功")

            request.urlretrieve(src,r"C:\Users\Administrator\Desktop\逻辑教育爬取文件\多线程ximalaya/"+title)

def main():
    page_queue = Queue(100) #页码队列
    data_queue = Queue(1000)#数据队列

    for page in range(1,18):#构造页码
        url = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=12576446&pageNum={}'.format(page)
        page_queue.put(url)

    for pn in range(5):
        t1 = Producer(page_queue, data_queue)
        t1.start()

    for data in range(5):
        t2 = Consumer(page_queue, data_queue)
        t2.start()
if __name__ == '__main__':
    main()

