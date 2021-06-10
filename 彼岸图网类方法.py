import requests
from fake_useragent import UserAgent
import time
from requests.exceptions import RequestException
from random import randint
from lxml import etree
import re
# from pypinyin import pinyin,lazy_pinyin
# import pypinyin

class DownLoad(object):
    """
    彼岸图网图片下载
    下载图片将保存在'D:\py图片\'目录下面
    注：本人文件操作不是很6，故文件夹基本是自己
    事先创建好的。
    """
    def __init__(self):
        self.base_url = 'http://pic.netbian.com'
        self.headers = {'User-Agent' : UserAgent().random}
        self.titles = [] # 存放图片名称
        self.hrefs = [] # 存放连接
        self.htmls = [] # 存放htmls
        self.name = [] # 存放搜索名称

    def get_search_url(self):
        """
        获取搜索界面的url
        并且将翻页后的url也提取出来
        :return: url
        """
        info = []
        search_base_urls = 'http://pic.netbian.com/'
        print('=' * 30)
        print("搜索关键字:\n")
        print("风景 美女 游戏 动漫 影视 明星 汽车 动物 人物 美食 宗教 背景\n")
        print('=' * 30)
        search_keys = input('请输入搜索的关键字的拼音：\n')
        self.name.append(search_keys)
        page_numbers = int(input("输入想要下载的页数：\n"))
        # lazy_pinyin(''.join(search_keys))
        # print(lazy_pinyin)
        search_url = search_base_urls + '4k' + search_keys + '/'
        # print(search_url)
        info.append(search_url)
        if page_numbers == 1:
            page_url = search_url
            # print(page_url)
            # yield page_url
        else:
            for page_number in range(page_numbers):
                page_url = search_url + 'index_{}.html'.format(page_number + 1)
                # print(page_url)
            # print(search_url)
                info.append(page_url)
        # print(info)
                # yield search_url,page_url
        return info
    def get_search_url_html(self,info):
        """
        解析搜索界面的url，得到网页原码
        :param info: 搜索界面的url
        :return: HTML
        """
        try:
            req = requests.get(info,headers = self.headers,timeout = 10)
            req.encoding = 'gbk'
            time.sleep(randint(1,2))
            if req.status_code == 200:
                return req.text
            else:
                return req.status_code
        except RequestException:
            return None
    def prase_html(self,html):
        """
        解析得到的HTML
        匹配图片的url
        找到图片的名字
        :param html: 解析的网页源代码
        :return: 
        """
        #http://pic.netbian.com/uploads/allimg/191127/191203-1574853123dddd.jpg
        #http://pic.netbian.com/uploads/allimg/191127/191203-1574853123ba79.jpg
        e = etree.HTML(html)
        titles = re.findall('<li><a .*?<b>(.*?)</b></a></li>',html)
        hrefs = e.xpath('//*[@id="main"]/div[3]/ul/li/a/@href')
        PageInfos = {

        }
        for title,href in zip(titles,hrefs):
            href = self.base_url + href
            # yield  {
            #     "title" : title,
            #     "href" : href
            # }
            self.titles.append(title)
            self.hrefs.append(href)
        # print(self.titles,self.hrefs)
    def save_img(self,start_time):
        """
        解析图片的url
        下载图片
        保存到指定的位置
        :param start_time: 程序开始计时
        :return: 
        """
        for url,title in zip(self.hrefs,self.titles):
            try:
                res = requests.get(url,headers = self.headers,timeout = 10)
                res.encoding = 'gbk'
                time.sleep(randint(0.5,1))
                if res.status_code == 200:
                    htmls = res.text
                    e = etree.HTML(htmls)
                    img_href = e.xpath('//*[@id="img"]/img/@src')
                    img_true_url = self.base_url + img_href[0]
                    rew = requests.get(img_true_url, headers=self.headers, timeout=10).content
                    try:
                        with open('D:\py图片\{}\{}.jpg'.format(self.name[0],title), 'wb') as f:
                            f.write(rew)
                            print('下载完毕：%s'%title)
                            print('用时{:.5f}秒'.format((time.perf_counter() - start_time)))
                    except:
                        print('文件打开出错')
                else:
                    print("错误")
            except RequestException:
                print('错误')
if __name__ == '__main__':
    print('=' * 45)
    print('下载图片将保存在’D:\py图片\(这里需要创建文件夹拼音，搜什么创建什么即可)\‘目录下面')
    print('=' * 45)
    d = DownLoad()
    start_time = time.perf_counter()
    infos = d.get_search_url()
    for info in infos:
        html = d.get_search_url_html(info)
        if html == 404:
            continue
        else:
            d.prase_html(html)
            d.save_img(start_time)


