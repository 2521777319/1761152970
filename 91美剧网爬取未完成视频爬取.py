import requests
from fake_useragent import UserAgent
from lxml import etree
# import io
# import sys
import time

def get_htmls(url,headers):
    req = requests.get(url,headers = headers,timeout = 30)
    req.encoding = 'utf-8'
    return req.text
def get_titles(htmls):
    e = etree.HTML(htmls)
    titles = e.xpath('//article[@class="u-movie"]/a/h2/text()')
    return titles
def get_urls(htmls):
    e = etree.HTML(htmls)
    urls = e.xpath('//article[@class="u-movie"]/a/@href')
    return urls
def prase_url(url,headers):
    req = requests.get(url, headers=headers, timeout=30)
    req.encoding = 'utf-8'
    req = req.text
    e = etree.HTML(req)
    tiqu_hrefs = e.xpath('//div[@class="vlink"]/a/@id')
    for info in tiqu_hrefs:
        base_href = info
        hrefs = 'https://91mjw.com/vplay/' + base_href + '.html'
        print(hrefs)
        get_contents(hrefs)
    print("============================")
def get_contents(hrefs):
    content = requests.get(hrefs).content
    save_contents(content,hrefs)
def save_contents(content,hrefs):
    with open(hrefs + 'mp4') as f:
        f.write(content)
def main():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    headers = {
        'User-Agent' : UserAgent().random
    }
    base_url = 'https://91mjw.com/'
    science_url = 'https://91mjw.com/category/all_mj/kehuanpian'
    htmls = get_htmls(science_url,headers)
    time.sleep(5)
    titles = get_titles(htmls)
    urls = get_urls(htmls)
    # print(titles,urls)
    for info in urls:
        url = info
        # print(url)
        prase_url(url,headers)
        time.sleep(5)


if __name__ == '__main__':
    main()
