import requests
from lxml import etree
import time

def get_one_page(url,headers):
    req = requests.get(url, headers=headers, timeout=30)
    time.sleep(5)
    if req.status_code == 200:
        return req.text
    return None

def parse_one_page(html):
    e = etree.HTML(html)
    infos = e.xpath('//*[@id="app"]/div/div/div[1]')
    for info in infos:
        rank = info.xpath('./dl/dd/i/text()')
        title = info.xpath('./dl/dd/div/div/div[1]/p[1]/a/text()')
        author = info.xpath('./dl/dd/div/div/div[1]/p[2]/text()')

        return "{} {} {}\n".format(rank,title,author)
def main():
    for i in range(0, 100, 10):
        url = 'https://maoyan.com/board/6?offset={}'.format(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'

            }
        html = get_one_page(url,headers)
        # print(html)
        parse_htmls = parse_one_page(html)
        print(parse_htmls)



if __name__ == '__main__':
    main()
