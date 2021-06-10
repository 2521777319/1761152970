import requests
import re
from fake_useragent import UserAgent
from requests.exceptions import RequestException
import time
from requests.adapters import DEFAULT_RETRIES
import random
class IpProxies:
    def __init__(self,num):
        """
        初始化信息
        :param num:
        """
        self.headers = {'User-Agent' : UserAgent().random} # 定义headers
        self.IP_dict = {} #定义的ip字典信息，可以打印看看ip的具体信息
        self.ip = [] #放入爬取的ip
        self.ip_type = [] #放入ip的HTTP或者HTTPS
        self.can_use = [] #放入可以使用的ip
        self.num = 1 #定义页数
        self.i = 0 #用来计可以使用的ip
        self.url = ['https://www.kuaidaili.com/free/inha/{}/'.format(str(num)),
                    'https://www.kuaidaili.com/free/intr/{}/'.format(str(num))] #高匿#普通
    def get_one_html(self):
        """
        爬取快代理上面的ip
        :return:
        """
        try:
            req = requests.get(random.choice(self.url),headers = self.headers,timeout = 10)
            req.encoding = 'utf-8'
            # print(req.text)
            # return req.text
        except RequestException:
            return None
        html = req.text
        '''
        ip里面的信息
        <td data-title="IP">144.52.197.73</td>
                    <td data-title="PORT">9999</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">山东省济宁市  电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2020-02-24 09:31:01</td>
        '''
        ip_list = re.findall('<td data-title="IP">(.*?)</td>',html)
        port_list = re.findall('<td data-title="PORT">(\d+)</td>',html)
        anonymous_list = re.findall('<td data-title="匿名度">(.*?)</td>',html)
        type_list = re.findall('<td data-title="类型">(.*?)</td>',html)
        # print(print(ip_list,port_list,type_list,anonymous_list))
        for info in zip(ip_list,port_list,type_list,anonymous_list):
            self.IP_dict['ip'] = info[0]
            self.IP_dict['port'] = info[1]
            self.IP_dict['types'] = info[2]
            self.IP_dict['anonymous'] = info[3]
            proxies = self.IP_dict['ip'] + ':' + self.IP_dict['port']
            # print(self.IP_dict['types'],proxies)
            self.ip.append(proxies)
            self.ip_type.append(self.IP_dict['types'])
        # print(self.ip,self.ip_type)

            # print(self.IP_dict)

    def test_ip(self):
        """
        检测ip是否能用
        :return:
        """
        requests.adapters.DEFAULT_RETRIES = 3
        # IP = random.choice(self.ip)
        for IP,TYPE in zip(self.ip,self.ip_type):
            thisProxy = "{}://".format(TYPE.lower()) + IP
            thisIP = "".join(IP.split(":")[0:1])
            # print(thisProxy)
            print(thisIP)
            try:
                res = requests.get(url="http://icanhazip.com/",timeout = 2,proxies={"{}".format(TYPE.lower()): thisProxy})
                proxyIP = res.text
                if (proxyIP == thisIP):
                    self.can_use.append(proxyIP)
                    self.i += 1
                    print("代理IP:'" + proxyIP + "'有效！")
                else:
                    print("代理IP无效！")
            except: print("代理IP无效！")
            continue

    def prase_page_num(self):
        """
        如果能用的ip池不超过十个就继续请求
        :return:
        """
        if str(self.i) < str(10):
            num = self.num + 1
            d = IpProxies(num)
            time.sleep(2)
            d.get_one_html()
            d.test_ip()
            d.prase_page_num()
        else:
            print(self.can_use)


if __name__ == '__main__':
    d = IpProxies(num = 1)
    time.sleep(2)
    d.get_one_html()
    # html = d.get_one_html()
    # d.prase_one_html()
    d.test_ip()
    d.prase_page_num()


