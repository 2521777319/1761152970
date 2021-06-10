import requests
from requests.exceptions import RequestException
from lxml import etree
from fake_useragent import UserAgent
import json
import time

#url = http://lcoc.top/bizhi/
# http://lcoc.top/bizhi/api.php?cid=360new&start=0&count=30
class bizhi(object):
    def __init__(self):
        self.base_url = 'http://lcoc.top/bizhi/api.php?cid=360new&start=0&count=30'
        self.headers = {'User-Agent':UserAgent().random}
        self.timeout = 2
        self.html = []#用来存放起始页json数据
        self.img_1600_900 = []
        self.img_1440_900 = []
        self.img_1366_768 =[]
        self.img_1280_800 = []
        self.img_1280_1024 = []
        self.img_1024_768 = []
        self.start_time = time.perf_counter()
    def prase_base_url(self):
        try:
            req = requests.get(self.base_url,headers = self.headers,timeout = self.timeout)
            if req.status_code == 200:
                req.encoding = 'utf-8'
                req = req.text
                self.html.append(req)
                # print(req)
            else:
                return 0
        except RequestException:
            print('解析基础页面失败')
    def get_urls(self):
        base_json = json.loads(self.html[0])
        # print(base_json)
        data = base_json['data']
        # print(data)
        for data in data:
            name = data['utag']
            # if name == '':
            #     name = data['tag']
            print(name)
            img_1600_900 = data['img_1600_900']
            self.img_1600_900.append(img_1600_900)
            img_1440_900 = data['img_1440_900']
            self.img_1440_900.append(img_1440_900)
            img_1366_768 = data['img_1366_768']
            self.img_1366_768.append(img_1366_768)
            img_1280_800 = data['img_1280_800']
            self.img_1280_800.append(img_1280_800)
            img_1280_1024= data['img_1280_1024']
            self.img_1280_1024.append(img_1280_1024)
            img_1024_768 = data['img_1024_768']
            self.img_1024_768.append(img_1024_768)
        # print(self.img_1280_1024,self.img_1024_768,self.img_1280_800,self.img_1366_768,
        #       self.img_1440_900,self.img_1600_900)
        # print(len(self.img_1600_900))

    def save_pc(self):
        print('到此已经获取到下载链接耗时{:.5f}s'.format(time.perf_counter()-self.start_time))

if __name__ == '__main__':
    b = bizhi()
    b.prase_base_url()
    b.get_urls()