import requests
from fake_useragent import UserAgent
import time
from random import randint
from requests.exceptions import RequestException
from lxml import etree


#在网页源代码中搜索‘charset’查看网页编码方式
def get_url_html(url):
    try:
        headers = {
            'User-Agent' : UserAgent().random
        }
        request = requests.get(url,headers = headers,timeout = 30)
        request.encoding = 'gbk'
        time.sleep(randint(3,10))
        if request.status_code == 200:
            return request.text
        return None
    except RequestException:
        return None

def prase_html(html):
    e = etree.HTML(html)
    title = e.xpath('//*[@id="list"]/dl/dd/a/text()')
    # print(title)
    href = e.xpath('//*[@id="list"]/dl/dd/a/@href')
    return title,href

def get_name(html):
    e = etree.HTML(html)
    name = e.xpath('//*[@id="info"]/h1/text()')
    return name

def prase_ture_html(href,title,name):
    try:
        headers = {
            'User-Agent' : UserAgent().random
        }
        request = requests.get(href,headers = headers,timeout = 30)
        request.encoding = 'gbk'
        if request.status_code == 200:
            e = etree.HTML(request.text)
            contents = e.xpath('//*[@id="content"]/text()')
            # print(contents[:])
            print('正在下载：%s' % name)
            for content in contents:
                content = content

                content = content.replace(u'\xa0', u'')
                with open('D:\小说下载\%s.txt'%title,'a+') as f:
                    f.write(content)
            print('下载完毕： %s'%title)
        return None
    except RequestException:
        return None


def explain():
    print("""
    使用前请详细阅读此说明：
    本脚本是对'https://www.52bqg.com/'网站小说的下载
    使用本脚本首先需要在此网站上搜索想要下载的小说并将小
    说页面的网址粘贴在本脚本当中并按下回车等待即可
    小说统一下载至‘D:\小说下载\’目录中，下载之前请创建
    该文档并整理好该目录中的文件。
    本脚本下载的小说文档均以txt形式保存，每一章节为一个
    txt文档，整个文档中含有的txt个数就是将要下载小说章
    节数目
    """)
    print("\033[0;31m%s\033[0m" % "    下载之前请确保创建目录‘D:\小说下载\’")

def main():
    explain()
    input_url = input("请输入想要下载小说的网址：\n")
    # url = 'https://www.52bqg.com/book_126534/'
    html = get_url_html(input_url)
    # print(html)
    true_info = prase_html(html)

    titles = true_info[0]
    hrefs = true_info[1]
    # name = true_info[2]
    # print(title,href)
    name = get_name(html)[0]
    # print(name)

    for href,title in zip(hrefs,titles):
        href = input_url + href
        prase_ture_html(href,title,name)


if __name__ == '__main__':
    main()
