import requests
from fake_useragent import UserAgent
from lxml import etree
import re
# import io
# import sys
import time


#https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=4&start={}.format(i)
def get_htmls(headers,url):
    req = requests.get(url,headers = headers,timeout = 30)
    req.encoding = 'utf-8'
    # print(req.text)
    return req.text


#/html/body/li/div/a/@href
def parse_urls(official_url,htmls):
    e = etree.HTML(htmls)
    titles = re.findall('<div class="vervideo-title">(.*?)</div>',htmls)
    content_url = e.xpath('/html/body/li/div/a/@href')
    # for info,title in zip(content_url,titles):
    #     info = official_url + info
    #     print(info,title)
    return content_url,titles
        # get_contents(info,headers)
#     for title in titles:
#         print(title)
#         get_contents(headers,title)

def get_contents(video_url,headers):
    req = requests.get(video_url, headers=headers, timeout=30)
    req.encoding = 'utf-8'
    # e = etree.HTML(req.text)
    ture_url = re.findall('srcUrl="(.*?)"',req.text)
    # print(ture_url)
    return ture_url
def get_allcontents(ture_url,headers,video_title):
    req = requests.get(ture_url, headers=headers, timeout=30).content
    with open(video_title + '.mp4' ,'wb') as f:
        f.write(req)
        print(video_title + '.mp4已经下载完毕')

def web_urls():
    web_urlss = []
    n = int(input('请输入想要爬取得页数：'))
    for i in range(n):
        i *= 12
        web_url = 'https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=4&start={}'.format(i)
        # print(web_url)
        # print('==============================')
        web_urlss.append(web_url)
    # print(web_urlss)
    return web_urlss

def main():
    i = 1
    headers = {
        'User-Agent' : UserAgent().random
    }
    official_url = 'https://www.pearvideo.com/'
    # recreat_url = 'https://www.pearvideo.com/category_4'
    web_url = web_urls()
    for infos in web_url:
        url = infos
        # print(url)
        htmls = get_htmls(headers,url)
        parse = list(parse_urls(official_url,htmls))
        video_urls = parse[0]
        video_title = parse[1]
        for video_url in video_urls:
            video_url = official_url + video_url
            true_video = get_contents(video_url,headers)
            for true_video,video_title in zip(true_video,video_title):
                get_allcontents(true_video,headers,video_title)
            # print(video_url)
            # print(video_title,video_urls)
            # print(parse[0])

        print('========================================')
        print('==         第' + str(i) + '页12个视频真实地址         ==')
        print('========================================')
        i += 1

    time.sleep(5)

if __name__ == '__main__':
    main()